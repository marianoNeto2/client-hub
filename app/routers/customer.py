from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.schemas.customer import CustomerCreate, CustomerRead, CustomerUpdate
from app.services import customer as customer_service


router = APIRouter(
    prefix="/customers",
    tags=["customers"],
    dependencies=[Depends(get_current_user)],
)

@router.post("/", response_model=CustomerRead, status_code=status.HTTP_201_CREATED)
def create_customer(
    payload: CustomerCreate,
    db: Session = Depends(get_db)
):
    customer = customer_service.create_customer(db, payload)
    if not customer:
        raise HTTPException(status_code=404, detail="Organization not found")
    return customer

@router.get("/{customer_id}", response_model=CustomerRead)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = customer_service.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.get("/", response_model=list[CustomerRead])
def list_customers(db: Session = Depends(get_db)):
    return customer_service.list_customers(db)

@router.patch("/{customer_id}", response_model=CustomerRead)
def update_customer(
    customer_id: int,
    payload: CustomerUpdate,
    db: Session = Depends(get_db)
):
    customer = customer_service.update_customer(db, customer_id, payload)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    deleted = customer_service.delete_customer(db, customer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Customer not found")
    return None
