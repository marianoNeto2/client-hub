from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Status(str, Enum):
    active = "active"
    invited = "invited"
    disabled = "disabled"


class MembershipBase(BaseModel):
    user_id: int
    organization_id: int
    role: str
    status: Status


class MembershipCreate(MembershipBase):
    pass


class MembershipUpdate(BaseModel):
    role: Optional[str] = None
    status: Optional[Status] = None


class MembershipRead(MembershipBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class MembershipRead(MembershipBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True
