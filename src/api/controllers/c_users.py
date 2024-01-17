from api.models.m_users import MUsers
from api.utils.LoggableObject import LoggableObject


class CUsers:
    """ Link between route and entity """

    def __init__(self):
        self.model = MUsers()
        self.logger = LoggableObject()

    def get_collection(self):
        self.logger.log_info('API', f"getting collection")
        return self.model.get_collection()
    
