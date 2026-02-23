from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.Corrections_notice import Corrections_notice as Corrections_notice_model
from app.schemas.Corrections_notice import CorrectionNoticeCreate

def get_corrections_notice(db: Session) -> List[Corrections_notice_model]:
    # returns all Notice action information taken by an officer
    return db.query(Corrections_notice_model).all()

def get_correction_notice(db: Session, NoticeID: int) -> Optional[Corrections_notice_model]:
    # returns all notice informaion relating to a specific noticeID
    return db.query(Corrections_notice_model).filter(Corrections_notice_model.NoticeID == NoticeID).first()

def get_violations_by_license(db: Session, drivers_license: int):
    return db.query(Corrections_notice_model).filter(
        Corrections_notice_model.Drivers_license == drivers_license
    ).all()

# Creates a new correction notice and saving it to the database
def create_correction_notice(db: Session, notice_in: CorrectionNoticeCreate) -> Corrections_notice_model:
    notice = Corrections_notice_model(
        Drivers_license = notice_in.Drivers_license,
        Notice_issue_date = notice_in.Notice_issue_date,
        District = notice_in.District,
        Location = notice_in.Location,
        Violation_time = notice_in.Violation_time,
        Violation_desc = notice_in.Violation_desc,
        OfficerID = notice_in.OfficerID,
    )
    db.add(notice)
    db.commit()
    db.refresh(notice)
    return notice