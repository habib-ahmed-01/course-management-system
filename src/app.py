from controllers.UserManager import UserManager
from utils.db import database_connection

if __name__ == '__main__':
    session = database_connection('postgresql')
    user = UserManager(session)
    user.get_user('8308dc90-1897-4bd4-b4be-5a7d59350a85')
