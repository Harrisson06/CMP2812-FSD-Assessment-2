from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from typing import List
from app.schemas.Officers import Officers
from app.crud.Officers import get_officer_by_license
from app.crud.Officers import get_officers

router = APIRouter()

@router.get("/officers/linked-to-license/{drivers_license}", response_model=Officers)
def read_officer_by_license(drivers_license: int, db: Session = Depends(get_db)):
    officer = get_officer_by_license(db, drivers_license)
    if not officer:
        # Raises a error code if there is no officer or license number in the database
        raise HTTPException(status_code=404, detail="No officer linked to this License")
    return officer

@router.get("/Officers", response_model=List[Officers])
def read_officers(db: Session = Depends(get_db)):
    return get_officers(db)