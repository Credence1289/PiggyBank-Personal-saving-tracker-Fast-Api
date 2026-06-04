from fastapi import APIRouter,HTTPException, Depends, status
from sqlalchemy.orm import Session
import logging
from app.models import models
from app.db.session import get_db
from app.core.gate import current_user
from app.schemas.piggybanks_schema import new_target

router = APIRouter()

logger = logging.getLogger(__name__)

@router.post("/users/piggybank/{piggybank_id}/deposit")
def create_piggybank_deposit(
    piggybank_id: int,
    amount: float,
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
    if amount <= 0:
        logger.warning("Amount must be greater than 0")
        raise HTTPException(status_code=400, detail="Amount must be greater than zero")

    piggybank.balance += amount


    new_transaction = models.Transaction(
        piggybank_id=piggybank.piggybank_id,
        type="Deposit",
        amount=amount,
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(piggybank)
    logger.info(f"Deposited {amount}rs in {piggybank_id}")
    return {
        "message": f"{amount}rs credited successfully into {piggybank.name}."
                   f"Your current balance is {piggybank.balance}rs"
    }


@router.post("/users/piggybank/{piggybank_id}/withdraw")
def create_piggybank_withdraw(
    piggybank_id: int,
    amount: float,
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
    if piggybank.balance < piggybank.target_amount:
        logger.warning(f"{piggybank.name} balance has not reached target amount yet")
        raise HTTPException(status_code=403, detail="Target not completed yet")
    if amount <= 0:
        logger.warning("Amount must be greater than 0")
        raise HTTPException(status_code=400, detail="Amount must be greater than zero")
    if piggybank.balance < amount:
        logger.warning(f"Insufficient funds in {piggybank_id}")
        raise HTTPException(status_code=400, detail="Insufficient funds")

    piggybank.balance -= amount

    new_transaction = models.Transaction(
        piggybank_id=piggybank.piggybank_id,
        type="Withdraw",
        amount=amount,
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(piggybank)

    logger.info("Withdrawn transaction")
    return {"message": f"{amount} successfully withdrawn from {piggybank.name}."}


@router.get("/users/piggybank/{piggybank_id}/transaction")
def show_transaction(
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

    transactions = (
        db.query(models.Transaction)
        .filter(models.Transaction.piggybank_id == piggybank_id)
        .all()
    )
    if not transactions:
        logger.warning("Transactions not found for ", piggybank_id)
        raise HTTPException(status_code=404, detail="No transactions found")
    return transactions

@router.put("/users/piggybank/{piggybank_id/new_target")
def set_new_target(
        data: new_target,
        db: Session = Depends(get_db),
        current: dict = Depends(current_user)
):
    piggybank = (
        db.query(models.PiggyBank)
        .filter(
        models.PiggyBank.piggybank_id == data.piggybank_id,
            models.PiggyBank.user_id == current["user"].user_id,
    ).first()
    )
    if not piggybank:
        logger.warning("PiggyBank not found for %s", data.piggybank_id)
        raise HTTPException(
            status_code=404,
            detail="PiggyBank not found"
        )

    if piggybank.balance > piggybank.target_amount:
        piggybank.target_amount = data.target_amount

        db.commit()
        db.refresh(piggybank)
        logger.info(f"Target of {piggybank.name} updated")
        raise HTTPException(
            status_code=200,
            detail=f"New target has successfully been set to {data.target_amount}rs",
        )
    else:
        logger.warning("Target has not completed yet")
        return {
            "message" : "Current target has not completed yet",
        }



















