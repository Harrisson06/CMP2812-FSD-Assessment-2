from app.db.base import Base
from app.db.session import engine

# Importing all tables to be automatically created
from app.models.Actions import Actions
from app.models.Corrections_notice import Corrections_notice
from app.models.Drivers import Drivers
from app.models.Notice_actions import Notice_actions
from app.models.officers import Officers
from app.models.Vehicles import Vehicles
from app.models.User import User

# Creating all tables that do not already exist.
def init_db():
    Base.metadata.create_all(bind=engine)