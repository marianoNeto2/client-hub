from sqlalchemy.orm import Session, selectinload

from app.models.organization import Organization


def create(db: Session, organization: Organization) -> Organization:
    db.add(organization)
    db.commit()
    db.refresh(organization)
    return organization


def get_by_id(db: Session, organization_id: int) -> Organization | None:
    return db.query(Organization).filter(Organization.id == organization_id).first()

def get_with_customers(db: Session, organization_id: int) -> Organization | None:
    return (
        db.query(Organization)
        .options(selectinload(Organization.customers))
        .filter(Organization.id == organization_id)
        .first()
    )


def list_all(db: Session) -> list[Organization]:
    return db.query(Organization).all()


def update(db: Session, organization: Organization, data: dict) -> Organization:
    for key, value in data.items():
        setattr(organization, key, value)
    db.add(organization)
    db.commit()
    db.refresh(organization)
    return organization


def delete(db: Session, organization: Organization) -> None:
    db.delete(organization)
    db.commit()
