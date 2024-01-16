from api.models.m_users import MUsers
from api.utils.LoggableObject import LoggableObject


class CUsers:
    """ Link between route and entity """

    def __init__(self):
        self.model = MUsers()
        self.logger = LoggableObject()

    def get_all_users(self):
        self.logger.log_info('API', f"getting all users and scores")
        return self.model.get_all_users()
    
    def add_user(self, request):
        print(request)
        self.logger.log_info('API', f"Add the user to the record")
        return self.model.add_user(request)
