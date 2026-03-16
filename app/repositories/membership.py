from sqlalchemy.orm import Session
from app.models.membership import Membership

def create(db: Session, membership: Membership) -> Membership:
    db.add(membership)
    db.commit()
    db.refresh(membership)
    return membership

def get_by_id(db: Session, membership_id: int) -> Membership | None:
    return db.query(Membership).filter(Membership.id == membership_id).first()

def list_all(db: Session) -> list[Membership]:
    return db.query(Membership).all()

def update(db: Session, membership: Membership, data: dict) -> Membership:
    for key, value in data.items():
        setattr(membership, key, value)
    db.add(membership)
    db.commit()
    db.refresh(membership)
    return membership

def delete(db: Session, membership: Membership) -> None:
    db.delete(membership)
    db.commit()

