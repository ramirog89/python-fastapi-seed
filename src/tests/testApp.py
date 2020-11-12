from os import path
from pytest import fixture
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.app import app
from src.app.database import Base, get_db

from src.app.services import AuthenticationService
from src.app.repositories.user import UserRepository, schema, model

TEST_ROOT_DIR = path.dirname(path.abspath(__file__))

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
  SQLALCHEMY_DATABASE_URL,
  connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

testingSession = TestingSessionLocal()

def get_db_test():
  try:
    db = TestingSessionLocal()
    yield db
  finally:
    db.close()

app.dependency_overrides[get_db] = get_db_test

testApp = TestClient(app)

tokenUserRole = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlcmVzYSIsImlkIjoyLCJyb2xlIjoidXNlciIsImlzX2FjdGl2ZSI6dHJ1ZX0.IcDu_2o0LJVVvs95AT6U-XYmniTX65AIlUI7qTzr0pI'
tokenLogin = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJpZCI6MSwicm9sZSI6ImFkbWluIiwiaXNfYWN0aXZlIjp0cnVlfQ.RuvR3-ALqgWUdFTawstqyT2chqG5pfyKRROIuYGOyV0'
invalidToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjIiLCJ1c2VybmFtZSI6InJhbWlybyIsImhhc2hlZF9wYXNzd29yZCI6InJhbWlyb25vdHJlYWxseWhhc2hlZCIsImlzX2FjdGl2ZSI6IlRydWUifQ.m13_7zIJovVkkZw27q_uBqPqqCCV2D0_Y5TMFsdmlmo'

userToken = 'Bearer ' + tokenUserRole
adminToken = 'Bearer ' + tokenLogin
invalidWebToken = 'Bearer ' + invalidToken

@fixture(scope="module", autouse=False)
def teardown(request):
  def clearDatabase():
    Base.metadata.drop_all(bind=engine)
  request.addfinalizer(clearDatabase)

userRepository = UserRepository(session=testingSession)

def setupAdmin():
  ''' Create a first user in the database '''
  user = schema.UserCreate(username='test', role='admin', password='test')
  userRepository.create(user)

def setupUser():
  ''' Create a first user in the database '''
  user = schema.UserCreate(username='tere', role='user', password='tere')
  userRepository.create(user)

def teardownUser():
  ''' Drop rows from user table '''
  testingSession.query(model.User).delete()
  testingSession.commit()
