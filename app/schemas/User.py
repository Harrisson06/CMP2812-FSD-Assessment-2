from pydantic import BaseModel, Field
from typing import Optional

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    role: Optional[str] = "Citizen"
    OfficerID: Optional[int] = Field(default=None, nullable=True)
    DriversLicense: Optional[int] = None

class User(UserBase):
    id: int
    role: str
    DriversLicense: Optional[int] = None

    class Config:
        from_attributes = True