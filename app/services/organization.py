from sqlalchemy.orm import Session
from app.models.organization import Organization
from app.repositories import organization as organization_repository
from app.schemas.organization import OrganizationCreate, OrganizationUpdate


def create_organization(db: Session, payload: OrganizationCreate) -> Organization:
    organization = Organization(**payload.model_dump())
    return organization_repository.create(db, organization)


def get_organization(db: Session, organization_id: int) -> Organization | None:
    return organization_repository.get_by_id(db, organization_id)


def list_organizations(db: Session) -> list[Organization]:
    return organization_repository.list_all(db)


def update_organization(
    db: Session,
    organization_id: int,
    payload: OrganizationUpdate,
) -> Organization | None:
    organization = organization_repository.get_by_id(db, organization_id)
    if not organization:
        return None
    data = payload.model_dump(exclude_unset=True)
    return organization_repository.update(db, organization, data)


def delete_organization(db: Session, organization_id: int) -> bool:
    organization = organization_repository.get_by_id(db, organization_id)
    if not organization:
        return False
    organization_repository.delete(db, organization)
    return True
