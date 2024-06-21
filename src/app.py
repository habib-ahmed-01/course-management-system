from controllers.UserManager import UserManager
from utils.db import database_connection

if __name__ == '__main__':
    session = database_connection('postgresql')
    user = UserManager(session)
    user.create_user(username='Habibul Bashar Ahmed', email="laru.y2k@gmail.com", password="password123#", role="Master")
