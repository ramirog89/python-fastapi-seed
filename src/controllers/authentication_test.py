from src.tests import testApp, token, user, teardownUser

from src.authentication.jwt import auth_jwt

def setup_module(module):
  ''' Create a first user in the database '''
  user('admin')

def test_valid_login(testApp, token):
    response = testApp.post(
        "/auth/login",
        json={"username": 'admintest', "password": 'admintest'}
    )
    assert response.status_code == 200
    assert response.json() == {'token': token('admin').raw }

def test_invalid_login(testApp):
    response = testApp.post(
        "/auth/login",
        json={"username": "wronguser", "password": "wrongpassword"}
    )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Username or password invalid.'}

def teardown_module(module):
  ''' Drop rows from user table '''
  teardownUser()
