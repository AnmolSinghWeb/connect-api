from uuid import UUID

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
    return errors

def validate_uuid(value):
    try:
        UUID(value, version=4)
    except ValueError:
        return False
    return True
