from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.repositories import organization as organization_repository
from app.schemas.customer import CustomerCreate, CustomerUpdate
from app.repositories import customer as customer_repository


def create_customer(db: Session, payload: CustomerCreate) -> Customer:
    organization = organization_repository.get_by_id(db, payload.organization_id)
    if not organization:
        return None
    customer = Customer(**payload.model_dump())
    return customer_repository.create(db, customer)

def get_customer(db: Session, customer_id: int) -> Customer | None:
    return customer_repository.get_by_id(db, customer_id)

def list_customers(db: Session) -> list[Customer]:
    return customer_repository.list_all(db)

def update_customer(
    db: Session,
    customer_id: int,
    payload: CustomerUpdate
) -> Customer | None:
    customer = customer_repository.get_by_id(db, customer_id)
    if not customer:
        return None
    data = payload.model_dump(exclude_unset=True)
    return customer_repository.update(db, customer, data)

def delete_customer(db: Session, customer_id: int) -> bool:
    customer = customer_repository.get_by_id(db, customer_id)
    if not customer:
        return False
    customer_repository.delete(db, customer)
    return True
    
