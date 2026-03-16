from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None

class UserRead(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True
