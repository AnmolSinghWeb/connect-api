from flask_restful import Resource
from api._utils.http_status import HttpStatus


class NtApiRoute(Resource):

    def __init__(self):
        self.controller = None
        self.user_id = None
        self.org_id = None

    def build_response(self, data, errors):
        if errors is None and data is None:
            return '', HttpStatus.INTERNAL_SERVER_ERROR
        if errors is not None:
            for err in errors:
                if 'not found' in err:
                    return {'errors': errors}, HttpStatus.NOT_FOUND
            return {'errors': errors}, HttpStatus.BAD_REQUEST
        if data == '':
            return '', HttpStatus.NO_CONTENT
        return data
