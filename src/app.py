from controllers.UserManager import UserManager
from utils.db import database_connection

if __name__ == '__main__':
    session = database_connection('postgresql')
    user = UserManager(session)
    user.delete_user('4a696898-3f18-4c19-ab9b-963cddbd43c6')
