from sqlalchemy.orm import Session
from app.models.user import User

def create(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def get_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def list_all(db: Session) -> list[User]:
    return db.query(User).all()

def update(db: Session, user: User, data: dict) -> User:
    for key, value in data.items():
        setattr(user, key, value)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def delete(db: Session, user: User) -> None:
    db.delete(user)
    db.commit()
