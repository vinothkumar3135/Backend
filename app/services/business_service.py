from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import business_repo


def get_or_404(db: Session, business_id: int, owner_id: int):
    biz = business_repo.get(db, business_id, owner_id)
    if not biz:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Business not found")
    return biz


def remove(db: Session, business_id: int, owner_id: int) -> None:
    business_repo.delete(db, get_or_404(db, business_id, owner_id))
