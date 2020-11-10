from pydantic import BaseModel

from .validator import validate, isRequired, isValidEmail

def test_email_validator():
  class TestSchema(BaseModel):
    name: str
    lastname: str
    email: str

  testUser = TestSchema(name="", lastname="", email="email")

  response = validate(testUser, {
    'name': [isRequired],
    'lastname': [isRequired],
    'email': [isRequired, isValidEmail]
  })

  assert response == {
    'name': ['is Required'],
    'lastname': ['is Required'],
    'email': ['The email address is not valid. It must have exactly one @-sign.']
  }

def test_with_multiple_validations():
  def raise_(e):
    raise e
  class TestSchema(BaseModel):
    name: str
    lastname: str
    email: str

  testUser = TestSchema(name="", lastname="", email="email")

  response = validate(testUser, {
    'name': [lambda a : raise_(Exception('Error 1')), lambda a : raise_(Exception('Error 2'))],
    'email': []
  })

  assert response == {
    'name': ['Error 1', 'Error 2'],
  }

def test_with_empty_contraints_and_not_defined_schema_keys():
  class TestSchema(BaseModel):
    name: str
    lastname: str
    email: str

  testUser = TestSchema(name="", lastname="", email="email")

  response = validate(testUser, {
    'name': [],
    'email': []
  })

  assert response == {}
