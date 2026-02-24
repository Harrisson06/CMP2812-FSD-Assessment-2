from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.Officers import Officers
from app.CRUD.Officers import get_officer_by_license

router = APIRouter()

@router.get("/officers/linked-to-license/{drivers_license}", response_model=Officers)
def read_officer_by_license(drivers_license: int, db: Session = Depends(get_db)):
    officer = get_officer_by_license(db, drivers_license)
    if not officer:
        raise HTTPException(status_code=404, detail="No officer linked to this License")
    return officer