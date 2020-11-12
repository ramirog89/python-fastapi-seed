from fastapi import Depends
from sqlalchemy import text

from src.database import get_db
from src.repositories import BaseRepository
from src.schemas import user as schema, pagination
from src.models import user as model
from src.utils.paginator import paginator

class UserRepository(BaseRepository):

  def getUserByUsernameAndPassword(self, username: str, password: str) -> model.User:
    return self.session.query(model.User).filter(model.User.username == username, model.User.hashed_password == password + 'notreallyhashed').first()

  def getUserById(self, user_id: int) -> model.User:
    return self.session.query(model.User).filter(model.User.id == user_id).first()

  def getUserByUsername(self, username: str) -> model.User:
    return self.session.query(model.User).filter(model.User.username == username).first()

  def getUserList(self, page: int, limit: int, sort: str, order: str) -> pagination.PaginationSchema[schema.User]:
    query = self.session.query(model.User)
    if sort is None and order is None:
      sort = 'id'
      order = 'asc'
    query = query.order_by(text(sort + " " + order))

    return paginator(query, page, limit)

  def create(self, user: schema.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = model.User(username=user.username, role=user.role, hashed_password=fake_hashed_password)
    self.session.add(db_user)
    self.session.commit()
    self.session.refresh(db_user)
    return db_user

  def update(self, db_user: schema.User, user: schema.UserUpdate) -> schema.User:
    fake_hashed_password = user.password + "notreallyhashed"
    db_user.username = user.username
    db_user.role = user.role
    db_user.is_active = user.is_active
    db_user.password = user.password
    self.session.commit()
    self.session.refresh(db_user)
    return db_user

  def delete(self, user: schema.User):
    self.session.delete(user)
    self.session.commit()