from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Actions(Base):
    ActionID = Column(Integer, Index=True, primary_key=True)
    Action_desc = Column(String(255))