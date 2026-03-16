from sqlalchemy.orm import Session
from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.repositories import user as user_repository

def create_user(db: Session, payload: UserCreate) -> User:
    data = payload.model_dump()
    data["password_hash"] = hash_password(data.pop("password"))
    user = User(**data)
    return user_repository.create(db, user)

def get_user(db: Session, user_id: int) -> User | None:
    return user_repository.get_by_id(db, user_id)

def get_user_by_email(db: Session, email: str) -> User | None:
    return user_repository.get_by_email(db, email)

def list_users(db: Session) -> list[User]:
    return user_repository.list_all(db)

def update_user(
        db: Session,
        user_id: int,
        payload: UserUpdate
) -> User | None:
    user = user_repository.get_by_id(db, user_id)
    if user is None:
        return None
    data = payload.model_dump(exclude_unset=True)
    return user_repository.update(db, user, data)

def delete_user(db: Session, user_id: int) -> bool:
    user = user_repository.get_by_id(db, user_id)
    if user is None:
        return False
    user_repository.delete(db, user)
    return True
