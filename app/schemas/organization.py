from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.schemas.customer import CustomerRead

class OrganizationBase(BaseModel):
    name: str 
    description: Optional[str] = None

class OrganizationCreate(OrganizationBase):
    pass

class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    
class OrganizationRead(OrganizationBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class OrganizationWithCustomers(OrganizationRead):
    customers: list[CustomerRead] = []
