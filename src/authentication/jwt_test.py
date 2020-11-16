from pytest import raises
from fastapi import HTTPException, status

from src.tests import userRepository, setupAdmin, teardownUser, getAuthorizationToken
from src.services.authentication import AuthenticationService

from .jwt import auth_jwt

def setup_module(module):
  setupAdmin()

def test_valid_token():
  authService = AuthenticationService(repository=userRepository)
  response = auth_jwt(getAuthorizationToken('admin'), authService)
  assert response == {'id': 1, 'is_active': True, 'role': 'admin', 'username': 'admintest'}

def test_invalid_token():
  authService = AuthenticationService(repository=userRepository)
  with raises(HTTPException) as error:
    auth_jwt(getAuthorizationToken('invalid'), authService)
  assert error.value.status_code == status.HTTP_403_FORBIDDEN

def test_token_not_match():
  authService = AuthenticationService(repository=userRepository)
  token = 'not valid token'
  
  with raises(HTTPException) as error:
    auth_jwt(token, authService)
  assert error.value.status_code == status.HTTP_401_UNAUTHORIZED

def test_token_jwt_incompatible():
  authService = AuthenticationService(repository=userRepository)
  token = 'Bearer token-jwt-incompatible'
  
  with raises(HTTPException) as error:
    auth_jwt(token, authService)
  assert error.value.status_code == status.HTTP_401_UNAUTHORIZED

def teardown_module(module):
  teardownUser()