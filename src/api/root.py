from flask_restful import Resource
from api._utils.http_status import HttpStatus

class Root(Resource):
    paths = [
        '/'
    ]

    def get(self):
        return '*** --- nt-api --- ***', HttpStatus.OK

def init(api_ref):
    api_ref.add_resource(Root, *Root.paths)
