from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create SQLAlchemy engine
engine = create_engine(
    'sqlite:///./sql_app.db', connect_args={"check_same_thread": False}
)

# Create SQLAlchemy Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
