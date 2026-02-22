from sqlalchemy.orm import Session
from typing import Optional
from app.models.User import User as UserModel
from app.schemas.User import UserCreate
from app.core.Security import hash_password

# Finds a user in the database using their email
def get_user_by_email(db: Session, email: str) -> Optional[UserModel]:
    # Filters stored emails for the one being used
    return db.query(UserModel).filter(UserModel.email == email).first()

# Creates a new user and saves them to the database in Users table
def create_user(db: Session, user_in: UserCreate) -> UserModel:
    user = UserModel(
        name=user_in.name,
        email=user_in.email,
        password_hash=hash_password(user_in.password), # Hashes the password before saving it
        role=user_in.role or "user", # If no role is placed defaults to user rather than a null field or error 
    )
    db.add(user)        # Add's the new user
    db.commit()         # Saves the new user to the database
    db.refresh(user)    # Refreshes the database to get a new ID 
    return user         # Returns the created user