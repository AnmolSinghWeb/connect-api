from flask import request
from api._types.ntapiroute import NtApiRoute
from api._middleware.validation import validate_scope, validate_token
from api.controllers.c_users import CUsers
from api._utils.http_status import HttpStatus
# import chromadb
# from chromadb.config import Settings

# client = chromadb.HttpClient(host='localhost', port=8000, settings=Settings(allow_reset=True, anonymized_telemetry=False))


#pylint: disable=too-many-return-statements
class RUsers(NtApiRoute):
    paths = [
        '/collection'
    ]
    method_decorators = [validate_token]

    def __init__(self):
        super().__init__()
        self.controller = CUsers()
        self.request_limit = 5000
        self.optimization_limit = 5000

    @validate_scope('foot_traffic.reports:read')
    def get(self, **kwargs):
        print('here')
        # collection = client.create_collection(name="my_collection")
        # collection = client.get_collection(name="my_collection")
        # collection.add(
        #     embeddings=[[1.2, 2.3, 4.5], [6.7, 8.2, 9.2]],
        #     documents=["This is a document", "This is another document"],
        #     metadatas=[{"source": "my_source"}, {"source": "my_source"}],
        #     ids=["id1", "id2"]
        # )
        # print(collection.get())
        data, errors = None, None
        data, errors = self.controller.get_collection()
        return self.build_response(data, errors)
    
    # def post(self, **kwargs):
    #     data, errors = None, None
    #     if isinstance(request.json, dict):
    #         data, errors = self.controller.add_user(request.json)
    #     return self.build_response(data, errors)