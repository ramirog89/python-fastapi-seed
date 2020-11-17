from src import models
from .database import engine, SessionLocal


# Register all application models under models/ directory
models.Base.metadata.create_all(bind=engine)


# DB getter for each request.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
