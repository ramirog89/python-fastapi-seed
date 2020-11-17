from fastapi import Depends
from src.database import get_db


class BaseRepository:
    session = None

    def __init__(self, session: get_db = Depends()):
        self.session = session
