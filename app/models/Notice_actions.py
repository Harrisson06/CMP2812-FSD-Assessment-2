from sqlalchemy import Column, Integer, ForeignKey
from app.db.base import Base

class NoticeActions(Base):
    NoticeID = Column(Integer, primary_key=True)
    ActionID = Column(Integer, ForeignKey)
