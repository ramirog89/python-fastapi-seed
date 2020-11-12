from fastapi import Depends

from src.app.repositories import UserRepository
from src.app.schemas import user as schema
from src.app.utils.validator import validate, isRequired

class UserBusinessLogicService:
  userRepository = None

  def __init__(
    self,
    userRepository: UserRepository = Depends(),
  ):
    self.userRepository = userRepository

  def getUserList(
    self,
    page: int = 0,
    limit: int = 10,
    sort: str = None,
    order: str = None
  ):
    return self.userRepository.getUserList(page, limit, sort, order)

  def getById(self, id: int):
    user = self.userRepository.getUserById(id)
    if user is not None:
      return user
    raise Exception('User does not exist')

  def create(self, user: schema.UserCreate):
    result = validate(user, {
      'username': [isRequired, self.userExist],
    })
    if len(result) == 0:
      return self.userRepository.create(user)
    raise Exception(result)

  def update(self, id: int, user: schema.UserUpdate):
    db_user = self.userRepository.getUserById(id)
    if db_user:
      result = validate(user, {
        'username': [isRequired],
      })
      if len(result) == 0:
        return self.userRepository.update(db_user, user)
      raise Exception(result)
    else:
      raise Exception("User does not exist")

  def delete(self, id: int):
    db_user = self.userRepository.getUserById(id)
    if db_user is not None:
      return self.userRepository.delete(db_user)
    raise Exception("User does not exist")

  def userExist(self, username: str):
    db_user = self.userRepository.getUserByUsername(username)
    if db_user:
      raise Exception('Username already exist')
    return True

