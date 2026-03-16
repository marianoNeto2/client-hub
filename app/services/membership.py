from sqlalchemy.orm import Session

from app.models.membership import Membership
from app.repositories import membership as membership_repository
from app.repositories import organization as organization_repository
from app.repositories import user as user_repository
from app.schemas.membership import MembershipCreate, MembershipUpdate

def create_membership(db: Session, payload: MembershipCreate) -> Membership:
    organization = organization_repository.get_by_id(db, payload.organization_id)
    if not organization:
        return None
    user = user_repository.get_by_id(db, payload.user_id)
    if not user:
        return None
    membership = Membership(**payload.model_dump())
    return membership_repository.create(db, membership)

def get_membership(db: Session, membership_id: int) -> Membership | None:
    return membership_repository.get_by_id(db, membership_id)

def list_memberships(db: Session) -> list[Membership]:
    return membership_repository.list_all(db)

def update_membership(
    db: Session,
    membership_id: int,
    payload: MembershipUpdate,
) -> Membership | None:
    membership = membership_repository.get_by_id(db, membership_id)
    if not membership:
        return None
    data = payload.model_dump(exclude_unset=True)
    return membership_repository.update(db, membership, data)

def delete_membership(db: Session, membership_id: int) -> None:
    membership = membership_repository.get_by_id(db, membership_id)
    if not membership:
        return False
    membership_repository.delete(db, membership)
    return True
