from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.Corrections_notice import Corrections_notice as Corrections_notice_model

def get_corrections_notice(db: Session) -> List[Corrections_notice_model]:
    # returns all Notice action information taken by an officer
    return db.query(Corrections_notice_model).all()

def get_correction_notice(db: Session, NoticeID: int) -> Optional[Corrections_notice_model]:
    # returns all notice informaion relating to a specific noticeID
    return db.query(Corrections_notice_model).filter(Corrections_notice_model.NoticeID == NoticeID).first()