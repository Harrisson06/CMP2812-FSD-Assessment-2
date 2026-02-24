from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.officers import Officers as OfficersModel

# Returns a list of all officers in the database
def get_officers(db: Session) -> List[OfficersModel]:
    return db.query(OfficersModel).all()

# Returns a specific officer linked to a drivers license in the correctons notice table
def get_officer_by_license(db: Session, drivers_license: int) -> Optional[OfficersModel]:
    from app.models.Corrections_notice import Corrections_notice
    return db.query(OfficersModel).join(
        Corrections_notice, Corrections_notice.OfficerID == OfficersModel.OfficerID
    ).filter(Corrections_notice.DriversLicense == drivers_license).first()