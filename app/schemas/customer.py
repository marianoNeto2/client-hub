from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    organization_id: int

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class CustomerRead(CustomerBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True
