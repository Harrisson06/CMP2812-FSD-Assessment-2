from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Vehicles(Base):
    Drivers_license = Column(Integer)
    Colour = Column(String(12))
    Make = Column(String(20))
    VIN = Column(String(17), primary_key=True)
    License_plate = Column(String(8))
    Registered_address = Column(String(20))
    State_registered = Column(String(20))
    Registered_year = Column(Integer)
    Car_type = Column(String(20))