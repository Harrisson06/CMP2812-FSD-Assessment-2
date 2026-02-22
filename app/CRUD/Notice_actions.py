from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.Notice_actions import Notice_actions as Notice_actions_model

def get_corrections_notice(db: Session):
    # returns all Correction notices 
    return db.query(Notice_actions_model).all()

def get_correction_notice(db: Session, NoticeID: int):
    # returns a specific notice relating to the notice ID
    return db.query(Notice_actions_model).filter(Notice_actions_model.NoticeID == NoticeID).first()