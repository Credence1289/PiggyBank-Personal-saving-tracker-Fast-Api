from fastapi import APIRouter,HTTPException, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
import logging
from datetime import timedelta

from app.schemas.refresh_token_schema import RefreshTokenReq
from app.core.security import hash_password, verify_password
from app.models import models
from app.db.session import get_db
from app.core.token import create_access_token ,decode_token
from app.core.gate import current_user
from app.schemas.users_schema import UserCreate, Token
from app.core.config import settings

router = APIRouter()

logger = logging.getLogger(__name__)

@router.post("/users")
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    existing = (
        db.query(models.User)
        .filter(
            (models.User.email == user.email) |
            (models.User.mobile_no == user.mobile_no)
        )
        .first()
    )
    if existing:
        logger.info("User already exists with this email or mobile number")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists with this email or mobile number"
        )

    new_user = models.User(
        name=user.name,
        mobile_no=user.mobile_no,
        email=user.email,
        hashed_password=hash_password(user.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    logger.info(f"New user created: {new_user.user_id}")
    return {
        "user_id": new_user.user_id,
        "message": "User created successfully"
    }


@router.post("/user/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = (
        db.query(models.User)
        .filter(models.User.email == form_data.username)
        .first()
    )
    if not user or not verify_password(form_data.password, user.hashed_password):
        logger.warning("Authentication failed for email %s", form_data.username)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token = create_access_token(user_id=user.user_id, role="user")
    refresh_token = create_access_token(
        user_id=user.user_id,
        refresh=True,
        expiry=timedelta(days=settings.REFRESH_TOKEN_EXPIRY),
        role="user"
    )
    logger.debug(f"Access Token generated for {user.user_id}")
    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer"
    )


@router.delete("/users/me")
def delete_user(current: dict = Depends(current_user), db: Session = Depends(get_db)):
    db.delete(current["user"])
    db.commit()
    logger.info(f"User {current['user'].user_id} deleted")
    return {"message": "User deleted successfully"}

@router.post("/user/refresh")
def refresh_access_token(
    data: RefreshTokenReq
):
    payload = decode_token(data.refresh_token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )

    if payload.get("refresh") is not True:
        raise HTTPException(
            status_code=401,
            detail="Not a refresh token"
        )

    new_access_token = create_access_token(
        user_id=payload["user_id"],
        role=payload["role"]
    )

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }