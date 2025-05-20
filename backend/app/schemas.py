# app/schemas.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class PortBase(BaseModel):
    name: str
    description: Optional[str] = None

class PortCreate(PortBase):
    pass

class PortResponse(PortBase):
    id: int
    status: str
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    ports: List[PortResponse] = []

    class Config:
        orm_mode = True
