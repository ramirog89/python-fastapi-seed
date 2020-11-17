from jwt import encode
from fastapi import Depends

from src.config import settings
from src.repositories.user import UserRepository
from src.schemas.user import User


class AuthenticationService:
    repository = None

    def __init__(self, repository: UserRepository = Depends(UserRepository)):
        self.repository = repository

    def userExist(self, id: int) -> bool:
        return bool(self.repository.getUserById(id))

    @staticmethod
    def encodeToken(user) -> str:
        return encode(User(**vars(user)).as_dict(), settings['JWT']['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    def login(self, username: str, password: str) -> User:
        user = self.repository.getUserByUsernameAndPassword(username, password)
        if user:
            return AuthenticationService.encodeToken(user)
        return False
