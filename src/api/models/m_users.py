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
from api.storage.entities.users.users import Users

class MUsers(NtApiModel):

    def __init__(self):
        super().__init__()
        self.storage_model = Users

    def get_all_users(self):
        return_data = None
        errors = None
        session = None
        try:
            session = session_factory()
            statement = session.query(self.storage_model)
            return_data = []
            for stat in statement:
                return_data.append(self.storage_model.get_dict(stat))
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
        return return_data, errors
    
    def add_user(self, request):
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