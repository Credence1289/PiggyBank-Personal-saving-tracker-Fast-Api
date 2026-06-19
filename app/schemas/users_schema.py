from pydantic import BaseModel, EmailStr,field_validator
from typing import Optional
from datetime import datetime

class User(BaseModel):
    user_id: Optional[int] = None
    name: str
    mobile_no: str
    email: EmailStr
    password: str | None = None

    @field_validator("password")
    @classmethod
    def check_pass(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit")
        if not any(char.islower() for char in value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(char.isupper() for char in value):
            raise ValueError("Password must contain at least one uppercase letter")
        return value

class UserCreate(BaseModel):
    name:str
    email:EmailStr
    mobile_no:str
    password:str

class Token(BaseModel):
    access_token : str
    refresh_token:str
    token_type : str = "bearer"