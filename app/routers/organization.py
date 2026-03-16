from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationRead,
    OrganizationUpdate,
)
from app.services import organization as organization_service

router = APIRouter(
    prefix="/organizations",
    tags=["organizations"],
    dependencies=[Depends(get_current_user)],
)


@router.post("/", response_model=OrganizationRead, status_code=status.HTTP_201_CREATED)
def create_organization(
    payload: OrganizationCreate,
    db: Session = Depends(get_db),
):
    return organization_service.create_organization(db, payload)


@router.get("/{organization_id}", response_model=OrganizationRead)
def get_organization(
    organization_id: int,
    db: Session = Depends(get_db),
):
    organization = organization_service.get_organization(db, organization_id)
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    return organization


@router.get("/", response_model=list[OrganizationRead])
def list_organizations(db: Session = Depends(get_db)):
    return organization_service.list_organizations(db)


@router.patch("/{organization_id}", response_model=OrganizationRead)
def update_organization(
    organization_id: int,
    payload: OrganizationUpdate,
    db: Session = Depends(get_db),
):
    organization = organization_service.update_organization(
        db, organization_id, payload
    )
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    return organization


@router.delete("/{organization_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_organization(
    organization_id: int,
    db: Session = Depends(get_db),
):
    deleted = organization_service.delete_organization(db, organization_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Organization not found")
    return None
