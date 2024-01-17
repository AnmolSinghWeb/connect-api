import math
import uuid
from sqlalchemy \
    import exc, and_, func
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.sql import text
from sqlalchemy import desc
from api.storage \
    import session_factory
from api._types.ntapimodel \
    import NtApiModel
import chromadb
from chromadb.config import Settings

class MUsers(NtApiModel):

    def __init__(self):
        super().__init__()
    
    def client(self):
        return chromadb.HttpClient(host='localhost', port=8000, settings=Settings(allow_reset=True, anonymized_telemetry=False))


    def get_collection(self):
        return_data = None
        errors = None
        session = None
        
        try:
            # collection = client.create_collection(name="my_collection")
            client = self.client()
            collection = client.get_collection(name="my_collection").get()
            # collection.add(
            #     embeddings=[[1.2, 2.3, 4.5], [6.7, 8.2, 9.2]],
            #     documents=["This is a document", "This is another document"],
            #     metadatas=[{"source": "my_source"}, {"source": "my_source"}],
            #     ids=["id1", "id2"]
            # )
            # print(collection.get())
            return_data = collection
        except exc.DatabaseError as exception:
            errors = [exception.statement]
            return_data = None
            print(exception)
        except exc.NoResultFound as exception:
            errors = ['No users found']
            print(exception)
        except exc.SQLAlchemyError as exception:
            return_data, errors = None, None
            print(exception)
        finally:
            print('finally')
        return return_data, errors
    
    # def add_user(self, request):
        return_data = None
        errors = None
        session = None
        try:
            session = session_factory()
            statment = insert(self.storage_model).values(request['data']).on_conflict_do_nothing()
            print(statment)
            session.execute(statment)
            session.commit()
            session.close()
        except exc.DatabaseError as exception:
            errors = [exception.statement]
            return_data = None
            print(exception)
        except exc.NoResultFound as exception:
            errors = ['No users found']
            print(exception)
        except exc.SQLAlchemyError as exception:
            return_data, errors = None, None
            print(exception)
        finally:
            if session:
                session.close()
        return_data = ['name1']
        return return_data, errors