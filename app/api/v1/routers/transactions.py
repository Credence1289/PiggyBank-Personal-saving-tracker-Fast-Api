from fastapi import APIRouter,HTTPException, Depends, status
from sqlalchemy.orm import Session

from app.models import models
from app.db.session import get_db
from app.core.gate import current_user
from app.schemas.piggybanks_schema import new_target

router = APIRouter()

@router.post("/users/piggybank/{piggybank_id}/deposit")
def create_piggybank_deposit(
    piggybank_id: int,
    amount: float,
    db: Session = Depends(get_db),
    current: dict = Depends(current_user),
):
    piggybank = (
        db.query(db_models.PiggyBank)
        .filter(
            db_models.PiggyBank.piggybank_id == piggybank_id,
            db_models.PiggyBank.user_id == current["user"].user_id,
        )
        .first()
    )
    if not piggybank:
        raise HTTPException(status_code=404, detail="PiggyBank not found")
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than zero")

    piggybank.balance += amount


    new_transaction = db_models.Transaction(
        piggybank_id=piggybank.piggybank_id,
        type="Deposit",
        amount=amount,
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(piggybank)

    return {
        "message": f"{amount} credited successfully into {piggybank.name}."
                   f"Your current balance is {piggybank.balance}"
    }


@router.post("/users/piggybank/{piggybank_id}/withdraw")
def create_piggybank_withdraw(
    piggybank_id: int,
    amount: float,
    db: Session = Depends(get_db),
    current: dict = Depends(current_user),
):
    piggybank = (
        db.query(db_models.PiggyBank)
        .filter(
            db_models.PiggyBank.piggybank_id == piggybank_id,
            db_models.PiggyBank.user_id == current["user"].user_id,
        )
        .first()
    )
    if not piggybank:
        raise HTTPException(status_code=404, detail="PiggyBank not found")
    if piggybank.balance < piggybank.target_amount:
        raise HTTPException(status_code=403, detail="Target not completed yet")
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than zero")
    if piggybank.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    piggybank.balance -= amount

    new_transaction = db_models.Transaction(
        piggybank_id=piggybank.piggybank_id,
        type="Withdraw",
        amount=amount,
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(piggybank)

    return {"message": f"{amount} successfully withdrawn from {piggybank.name}."}


@router.get("/users/piggybank/{piggybank_id}/transaction")
def show_transaction(
    piggybank_id: int,
    db: Session = Depends(get_db),
    current: dict = Depends(current_user),
):
    piggybank = (
        db.query(db_models.PiggyBank)
        .filter(
            db_models.PiggyBank.piggybank_id == piggybank_id,
            db_models.PiggyBank.user_id == current["user"].user_id,
        )
        .first()
    )
    if not piggybank:
        raise HTTPException(status_code=404, detail="PiggyBank not found")

    transactions = (
        db.query(db_models.Transaction)
        .filter(db_models.Transaction.piggybank_id == piggybank_id)
        .all()
    )
    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found")

    return transactions

@router.put("/users/piggybank/{piggybank_id/new_target")
def set_new_target(
        data: new_target,
        db: Session = Depends(get_db),
        current: dict = Depends(current_user)
):
    piggybank = (
        db.query(db_models.PiggyBank)
        .filter(
        db_models.PiggyBank.piggybank_id == data.piggybank_id,
            db_models.PiggyBank.user_id == current["user"].user_id,
    ).first()
    )
    if not piggybank:
        raise HTTPException(
            status_code=404,
            detail="PiggyBank not found"
        )

    if piggybank.balance > piggybank.target_amount:
        piggybank.target_amount = data.target_amount

        db.commit()
        db.refresh(piggybank)

        raise HTTPException(
            status_code=200,
            detail=f"New target has successfully been set to {data.target_amount}rs",
        )
    else:
        return {
            "message" : "Current target has not completed yet",
        }



















