from fastapi import Depends

from src.repositories import UserRepository
from src.schemas import user as schema
from src.utils.validator import validate, isRequired


class UserBusinessLogicService:
    '''
        UserBusinessLogicService class contains all the logic related to the user.
        Is a middleware between the controller and the repository that validate or
        do business logic related to a specific endpoint and is the one that will
        throw an Exception in case the information is not possible to be retrived
        or return the requested data
    '''
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
