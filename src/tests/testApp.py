from os import path
from pytest import fixture
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src import app
from src.database import Base, get_db

from src.services.authentication import AuthenticationService
from src.repositories.user import UserRepository, schema, model

TEST_ROOT_DIR = path.dirname(path.abspath(__file__))
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
  SQLALCHEMY_DATABASE_URL,
  connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

testingSession = TestingSessionLocal()
userRepository = UserRepository(session=testingSession)

userDict = {
  'admin': schema.User(id=1, username='admintest', role='admin', is_active=True),
  'supservisor': schema.User(id=2, username='supervisortest', role='supervisor', is_active=True),
  'user': schema.User(id=3, username='usertest', role='user', is_active=True)
}

def get_db_test():
  try:
    db = TestingSessionLocal()
    yield db
  finally:
    db.close()

app.dependency_overrides[get_db] = get_db_test

class TokenTest:
  def __init__(self, token):
    self.raw = token
    self.auth = 'Bearer ' + token

def getToken(name: str) -> str:
  if name in userDict:
    return AuthenticationService.encodeToken(userDict[name])
  return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjIiLCJ1c2VybmFtZSI6InJhbWlybyIsImhhc2hlZF9wYXNzd29yZCI6InJhbWlyb25vdHJlYWxseWhhc2hlZCIsImlzX2FjdGl2ZSI6IlRydWUifQ.m13_7zIJovVkkZw27q_uBqPqqCCV2D0_Y5TMFsdmlmo'

def user(role: str) -> None:
  user = schema.UserCreate(username=userDict[role].username, password=role + 'test', role=userDict[role].role)
  userRepository.create(user)

def teardownUser() -> None:
  ''' Drop rows from user table '''
  testingSession.query(model.User).delete()
  testingSession.commit()

@fixture
def testApp():
  return TestClient(app)

@fixture
def token():
  def _getToken(name: str = 'admin') -> TokenTest:
    return TokenTest(getToken(name))
  return _getToken
