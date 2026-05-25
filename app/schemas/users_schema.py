from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class User(BaseModel):
    user_id: Optional[int] = None
    name: str
    mobile_no: str
    email: EmailStr
    password: str | None = None

class UserCreate(BaseModel):
    name:str
    email:EmailStr
    mobile_no:str
    password:str

class Token(BaseModel):
    access_token : str
    token_type : str = "bearer"