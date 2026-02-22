from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.Corrections_notice import Corrections_notice as Corrections_notice_model

def get_corrections_notice(db: Session):
    # returns all Correction notices 
    return db.query(Corrections_notice_model).all()

def get_correction_notice(db: Session, NoticeID: int):
    # returns a specific notice relating to the notice ID
    return db.query(Corrections_notice_model).filter(Corrections_notice_model.NoticeID == NoticeID).first()