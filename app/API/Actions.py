from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.Actions import Actions
from app.CRUD.Actions import get_action

router = APIRouter()
@router.get("/actions/{action_id}", response_model=Actions)

def read_action(action_id: int, db: Session = Depends(get_db)):
    action = get_action(db, ActionID=action_id)
    if not action:
        raise HTTPException(status_code=404, detail="ActionID not found")
    return action