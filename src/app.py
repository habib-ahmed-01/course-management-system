from models.Users import User
from utils.db import database_connection
from sqlmodel import text
from controllers.UserManager import UserManager

if __name__ == '__main__':
    session = database_connection('postgresql')
    # print("Connection successful")
    # Use the User class from the users module
    user = UserManager(session)
    user.create_user('Habib', 'hahmed.y2k@gmail.com', 'password', 'role')

    #session.add(user)
