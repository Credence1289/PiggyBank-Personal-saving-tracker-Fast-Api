from fastapi import APIRouter,HTTPException, Depends, status
from sqlalchemy.orm import Session
import logging

from app.core.security import hash_password, verify_password
from app.models import models
from app.db.session import get_db
from app.core.gate import current_user
from app.schemas.piggybanks_schema import PiggyBankCreate, new_target

router = APIRouter()

logger = logging.getLogger(__name__)

@router.post("/users/piggybank")
def create_piggybank(
    data: PiggyBankCreate,
    db: Session = Depends(get_db),
    current: dict = Depends(current_user),
):
    piggybank = models.PiggyBank(
        user_id=current["user"].user_id,
        hashed_passwordpb=hash_password(data.passwordpb),
        name=data.name,
        target_amount=data.target_amount,
        balance=0.0,
    )
    db.add(piggybank)
    db.commit()
    db.refresh(piggybank)
    logger.info("PiggyBank created for %s", current['user'].user_id)
    return {
        "piggybank_id": piggybank.piggybank_id,
        "message": "PiggyBank created successfully",
    }


@router.delete("/users/piggybank/{piggybank_id}")
def delete_piggybank_id(
    piggybank_id: int,
    name: str,
    passwordpb: str,
    db: Session = Depends(get_db),
    current: dict = Depends(current_user),
):
    piggybank = (
        db.query(models.PiggyBank)
        .filter(
            models.PiggyBank.piggybank_id == piggybank_id,
            models.PiggyBank.user_id == current["user"].user_id,
            models.PiggyBank.name == name,
        )
        .first()
    )
    if not piggybank:
        logger.warning("PiggyBank not found for %s", piggybank_id)
        raise HTTPException(status_code=404, detail="PiggyBank not found")

    if not verify_password(passwordpb, piggybank.hashed_passwordpb):
        logger.warning("Authentication failed for deleting piggybank %s", piggybank_id)
        raise HTTPException(status_code=401, detail="Invalid credentials")

    db.delete(piggybank)
    db.commit()
    logger.info("PiggyBank deleted%s", piggybank_id)
    return {"message": "PiggyBank successfully deleted"}


@router.get("/users/piggybank")
def show_all_piggy(db: Session = Depends(get_db), current: dict = Depends(current_user)):
    piggybanks = (
        db.query(models.PiggyBank)
        .filter(models.PiggyBank.user_id == current["user"].user_id)
        .all()
    )
    if not piggybanks:
        logger.warning("PiggyBank not found")
        raise HTTPException(status_code=404, detail="No piggybanks found")

    return [
        {
            "piggybank_id": p.piggybank_id,
            "name": p.name,
            "balance": p.balance,
        }
        for p in piggybanks
    ]


@router.get("/users/piggybank/{piggybank_id}")
def show_piggy(
    piggybank_id: int,
    db: Session = Depends(get_db),
    current: dict = Depends(current_user),
):
    piggybank = (
        db.query(models.PiggyBank)
        .filter(
            models.PiggyBank.piggybank_id == piggybank_id,
            models.PiggyBank.user_id == current["user"].user_id,
        )
        .first()
    )
    if not piggybank:
        logger.warning("PiggyBank not found for %s", piggybank_id)
        raise HTTPException(status_code=404, detail="PiggyBank not found")

    return {
        "piggybank_id": piggybank.piggybank_id,
        "user_id": piggybank.user_id,
        "name": piggybank.name,
        "balance": piggybank.balance,
        "target_amount": piggybank.target_amount,
        "is_target_active": piggybank.is_target_active,
    }

