from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.models import User
from app.dependencies.deps import get_current_user, get_db
from app.repositories import business_repo
from app.schemas.business import BusinessCreate, BusinessOut
from app.services import business_service

router = APIRouter(prefix="/api/businesses", tags=["businesses"])


@router.get("", response_model=list[BusinessOut])
def list_businesses(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return business_repo.list_for_owner(db, user.id)


@router.post("", response_model=BusinessOut, status_code=status.HTTP_201_CREATED)
def create_business(data: BusinessCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return business_repo.create(db, user.id, data.name, data.description)


@router.get("/{business_id}", response_model=BusinessOut)
def get_business(business_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return business_service.get_or_404(db, business_id, user.id)


@router.delete("/{business_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_business(business_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    business_service.remove(db, business_id, user.id)
