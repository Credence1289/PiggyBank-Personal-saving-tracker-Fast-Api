from pydantic import BaseModel, field_validator
from typing import Optional

class PiggyBank(BaseModel):
    piggybank_id: Optional[int] = None
    user_id: int
    name:str
    target_amount: float
    balance: float = 0.0
    is_target_active: bool = True

    model_config ={
        "from_attributes" : True
    }

class PiggyBankCreate(BaseModel):
    name:str
    target_amount:float
    passwordpb:str

    @field_validator("passwordpb")
    @classmethod
    def check_pass(cls, value):
        if type(value) is None:
            raise value
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters long")
        return value

class new_target(BaseModel):
    target_amount:int

class PiggyBankDelete(BaseModel):
    piggybank_id:int
    name:str
    passwordpb:str

