from typing import Generic, List, Dict, Callable
from email_validator import validate_email, EmailNotValidError
from functools import reduce

class ErrorField:
  field: List[str]

class ValidationError:
  errors: List[ErrorField]

def isRequired(value: str):
  if value is None or type(value) is str and len(value) == 0:
    raise Exception('is Required')
  return True

def isValidEmail(value: str):
  try:
    return validate_email(value)
  except EmailNotValidError as error:
    raise Exception(str(error))

def catchError(rule, value):
  try:
    rule(value)
  except Exception as error:
    return str(error)

def validateField(accumulator, item):
  result = [y for rule in item['rules'] if (y := catchError(rule, item['value'])) is not None]
  if len(result) > 0:
    return { **accumulator, str(item['key']): result }
  return accumulator

def validate(schema, constraints: Dict[str, List[Callable]]) -> ValidationError:
  fields = vars(schema)
  return reduce(validateField, [{'key': field, 'value': fields[field], 'rules': constraints[field] if field in constraints else [] } for field in fields.keys()], {})
