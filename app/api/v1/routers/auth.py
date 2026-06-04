from fastapi import APIRouter,HTTPException, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
import logging

from app.core.security import hash_password, verify_password
from app.models import models
from app.db.session import get_db
from app.core.token import create_access_token
from app.core.gate import current_user
from app.schemas.users_schema import UserCreate, Token

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

    logger.info(f"New user created: {new_user}")
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
        logger.warning("Authentication failed for email%s", user.email)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token = create_access_token(user_id=user.user_id, role="user")
    logger.debug(f"Access Token generated for {user.user_id}")
    return Token(access_token=access_token, token_type="bearer")


@router.delete("/users")
def delete_user(current: dict = Depends(current_user), db: Session = Depends(get_db)):
    db.delete(current["user"])
    db.commit()
    logger.info(f"User {current['user'].user_id} deleted")
    return {"message": "User deleted successfully"}