from uuid import UUID
from sqlalchemy.sql.sqltypes import \
    BIGINT, BigInteger, \
    INTEGER, Integer, \
    FLOAT, Float, \
    VARCHAR, String, \
    BOOLEAN, Boolean, \
    JSON

def validate_token(function):
    def wrapper(*args, **kwargs):
        # validate token
        #   token inside: request.headers.get('Authorization'))
        print('call: validate_token')
        return function(*args, **kwargs)
    return wrapper

def validate_scope(route_scope):
    def decorator(function):
        def wrapper(*args, **kwargs):
            # validate scope
            print('call: validate_scope')
            print('scope:', route_scope)
            return function(*args, **kwargs)
        return wrapper
    return decorator

def validate_generic_data(data, columns, ignored_key, validate_field_presence=True):
    errors = []
    for key, value in columns.items():
        if key in ignored_key:
            continue
        if key not in data or value is None:
            if validate_field_presence:
                errors.append(f'{key}: missing and cannot be null')
            continue
        if isinstance(value.type, (BIGINT, INTEGER, FLOAT, BigInteger, Integer, Float)):
            if not isinstance(data[key], (int, float)):
                errors.append(f'{key}: needs to be a JSON number')
        if isinstance(value.type, (String, VARCHAR)):
            if not isinstance(data[key], str):
                errors.append(f'{key}: needs to be a JSON string')
        if isinstance(value.type, (BOOLEAN, Boolean)):
            if not isinstance(data[key], bool):
                errors.append(f'{key}: needs to be a JSON boolean')
        if isinstance(value.type, JSON):
            if not isinstance(data[key], (dict, list)):
                errors.append(f'{key}: needs to be a valid JSON Object or Array')
    return errors

def validate_uuid(value):
    try:
        UUID(value, version=4)
    except ValueError:
        return False
    return True
