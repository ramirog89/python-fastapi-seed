from jwt import encode
from fastapi import Depends

from src.app.config import settings
from src.app.repositories.user import UserRepository
from src.app.schemas.user import User
from src.app.models.user import UserRole

class AuthenticationService:
  repository = None

  def __init__(self, repository: UserRepository = Depends(UserRepository)):
    self.repository = repository

  def userExist(self, id: int) -> bool:
    return bool(self.repository.getUserById(id))
  
  def login(self, username: str, password: str) -> User:
    user = self.repository.getUserByUsernameAndPassword(username, password)
    if user:
      return encode(User(**vars(user)).as_dict(), settings['JWT']['SECRET_KEY'], algorithm='HS256').decode('utf-8')
    return False
