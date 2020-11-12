from pydantic import BaseModel
from src.app.models.user import UserRole

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    role: UserRole

class UserUpdate(UserCreate):
    is_active: bool

class User(UserBase):
    id: int
    role: UserRole
    is_active: bool

    def as_dict(self):
      return { 'username': self.username, 'id': self.id, 'role': UserRole(self.role).value, 'is_active': self.is_active }

    class Config:
        orm_mode = True