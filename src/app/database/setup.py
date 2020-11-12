from fastapi import Request

from src.app import models
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
