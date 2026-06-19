from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime


class Transaction(BaseModel):
    transaction_id: Optional[int] = None
    piggybank_id: int
    name:str
    type: str  # "deposit" or "withdraw"
    amount: float
    time_stamp : Optional[datetime] = None

