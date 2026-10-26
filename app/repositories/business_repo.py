from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models import Business


def list_for_owner(db: Session, owner_id: int) -> list[Business]:
    return list(db.scalars(select(Business).where(Business.owner_id == owner_id)))


def get(db: Session, business_id: int, owner_id: int) -> Business | None:
    return db.scalar(select(Business).where(Business.id == business_id, Business.owner_id == owner_id))


def create(db: Session, owner_id: int, name: str, description: str) -> Business:
    biz = Business(owner_id=owner_id, name=name, description=description)
    db.add(biz)
    db.commit()
    db.refresh(biz)
    return biz


def delete(db: Session, biz: Business) -> None:
    db.delete(biz)
    db.commit()
