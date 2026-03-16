from sqlalchemy.orm import Session
from app.models.customer import Customer


def create(db: Session, customer: Customer) -> Customer:
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def get_by_id(db: Session, customer_id: int) -> Customer | None:
    return db.query(Customer).filter(Customer.id == customer_id).first()

def list_all(db: Session) -> list[Customer]:
    return db.query(Customer).all()

def update(db: Session, customer: Customer, data: dict) -> Customer:
    for key, value in data.items():
        setattr(customer, key, value)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def delete(db: Session, customer: Customer) -> None:
    db.delete(customer)
    db.commit()