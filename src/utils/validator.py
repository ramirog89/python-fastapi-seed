from typing import List, Dict, Callable, Any
from email_validator import validate_email, EmailNotValidError
from functools import reduce


class ErrorField:
    key: str
    value: Any
    rules: List[str]


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
        return {**accumulator, str(item['key']): result}
    return accumulator


def validate(schema, constraints: Dict[str, List[Callable]]) -> ValidationError:
    '''
        validate util function is a custom way to add validators to a schema.
        @schema: Any registered scheme in the application
        @constraints: dictionary of keys with a list of functions that will return True if valid or raise Exception if not valid.
            ej: { username: [existUsername, isRequired], email: [isValidEmail] }
        @return: { username: ['username already exists'], email: ['email is invalid'] }
    '''
    fields = vars(schema)
    return reduce(validateField, [{'key': field, 'value': fields[field], 'rules': constraints[field] if field in constraints else []} for field in fields.keys()], {})
