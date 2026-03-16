from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.schemas.membership import (
    MembershipCreate,
    MembershipRead,
    MembershipUpdate,
)
from app.services import membership as membership_service

router = APIRouter(
    prefix="/memberships",
    tags=["memberships"],
    dependencies=[Depends(get_current_user)],
)

@router.post("/", response_model=MembershipRead, status_code=status.HTTP_201_CREATED)
def create_membership(
    payload: MembershipCreate,
    db: Session = Depends(get_db)
):
    membership = membership_service.create_membership(db, payload)
    if not membership:
        raise HTTPException(status_code=404, detail="User or organization not found")
    return membership

@router.get("/{membership_id}", response_model=MembershipRead)
def get_membership(
    membership_id: int,
    db: Session = Depends(get_db)
):
    membership = membership_service.get_membership(db, membership_id)
    if not membership:
        raise HTTPException(status_code=404, detail="Membership not found")
    return membership

@router.get("/", response_model=list[MembershipRead])
def list_memberships(db: Session = Depends(get_db)):
    return membership_service.list_memberships(db)

@router.patch("/{membership_id}", response_model=MembershipRead)
def update_membership(
    membership_id: int,
    payload: MembershipUpdate,
    db: Session = Depends(get_db)
):
    membership = membership_service.update_membership(db, membership_id, payload)
    if not membership:
        raise HTTPException(status_code=404, detail="Membership not found")
    return membership

@router.delete("/{membership_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_membership(
    membership_id: int,
    db: Session = Depends(get_db)
):
    deleted = membership_service.delete_membership(db, membership_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Membership not found")
    return None
