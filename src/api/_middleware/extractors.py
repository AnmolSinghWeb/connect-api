from flask import request

def extract_org_and_user(function):
    def wrapper(*args, **kwargs):
        self = args[0]
        self.org_id = request.headers.get('x-nt-o')
        self.user_id = request.headers.get('x-nt-u')
        return function(*args, **kwargs)
    return wrapper
