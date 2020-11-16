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

def get_db_test():
  try:
    db = TestingSessionLocal()
    yield db
  finally:
    db.close()

app.dependency_overrides[get_db] = get_db_test
testApp = TestClient(app)

userDict = {
  'admin': schema.User(id=1, username='admintest', role='admin', is_active=True),
  'supservisor': schema.User(id=2, username='supervisortest', role='supervisor', is_active=True),
  'user': schema.User(id=3, username='usertest', role='user', is_active=True)
}

def getToken(name='admin'):
  if name == 'invalid':
    return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjIiLCJ1c2VybmFtZSI6InJhbWlybyIsImhhc2hlZF9wYXNzd29yZCI6InJhbWlyb25vdHJlYWxseWhhc2hlZCIsImlzX2FjdGl2ZSI6IlRydWUifQ.m13_7zIJovVkkZw27q_uBqPqqCCV2D0_Y5TMFsdmlmo'
  return AuthenticationService.encodeToken(userDict[name])

def getAuthorizationToken(name='admin'):
  return 'Bearer ' + getToken(name)

def setupAdmin():
  ''' Create a first user in the database '''
  user = schema.UserCreate(username=userDict['admin'].username, password='admintest', role=userDict['admin'].role)
  userRepository.create(user)

def setupUser():
  ''' Create a first user in the database '''
  user = schema.UserCreate(username=userDict['user'].username, password='usertest', role=userDict['user'].role)
  userRepository.create(user)

def teardownUser():
  ''' Drop rows from user table '''
  testingSession.query(model.User).delete()
  testingSession.commit()
