from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.User import User, UserCreate
from app.CRUD import User as Crud_user

router = APIRouter(prefix="/Users", tags=["Users"])

@router.post("/", response_model=User, status_code=201)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    existing = Crud_user.get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already in use")
    return Crud_user.create_user(db, user_in)

