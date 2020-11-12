import enum
from sqlalchemy import Boolean, Column, Integer, String, Table, Enum

from src.app.database import Base

class UserRole(str, enum.Enum):
  USER: str = 'user'
  SUPERVISOR: str = 'supervisor'
  ADMIN: str = 'admin'

class User(Base):
  __tablename__ = "user"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True)
  hashed_password = Column(String)
  role = Column(Enum(UserRole), default=UserRole.USER)
  is_active = Column(Boolean, default=True)
