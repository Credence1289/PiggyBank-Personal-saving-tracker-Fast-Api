from pydantic import BaseModel, EmailStr
from typing import Optional

class PiggyBank(BaseModel):
    piggybank_id: Optional[int] = None
    user_id: int
    passwordpb:str | None = None
    name:str
    target_amount: float
    balance: float = 0.0
    is_target_active: bool = True

class PiggyBankCreate(BaseModel):
    name:str
    target_amount:float
    passwordpb:str

class new_target(BaseModel):
    piggybank_id: Optional[int] = None
    target_amount:int