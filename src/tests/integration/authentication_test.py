from src.tests import app, testApp, testingSession, setupAdmin, teardownUser, tokenLogin
from src.app.authentication.jwt import auth_jwt

def setup_module(module):
  ''' Create a first user in the database '''
  setupAdmin()

def test_valid_login():
    response = testApp.post(
        "/auth/login",
        json={"username": 'test', "password": 'test'}
    )
    assert response.status_code == 200
    assert response.json() == {'token': tokenLogin }

def test_invalid_login():
    response = testApp.post(
        "/auth/login",
        json={"username": "wronguser", "password": "wrongpassword"}
    )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Username or password invalid.'}

def teardown_module(module):
  ''' Drop rows from user table '''
  teardownUser()
