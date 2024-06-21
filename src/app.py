from controllers.UserManager import UserManager
from utils.db import database_connection

if __name__ == '__main__':
    session = database_connection('postgresql')
    user = UserManager(session)
    print(user.get_all())
