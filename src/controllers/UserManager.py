# Methods: create_user, update_user, delete_user
from passlib.hash import bcrypt
from sqlmodel import text


class UserManager:
    def __init__(self, session):
        self._session = session

    def create_user(self, username: str, email: str, password: str, role: str):
        hashed_password = bcrypt.hash(password)
        statement: text = text(
            f"""INSERT INTO users (username, email, password, role) values ('{username}', '{email}', '{hashed_password}', '{role}')""")
        self._session.exec(statement)
        self._session.commit()

    def update_user(self, user_id: str, **kwargs: str):
        update_params: list = []
        kwargs['password'] = bcrypt.hash(kwargs['password'])
        for key, value in kwargs.items():
            update_string: str = f"{key}='{value}'"
            update_params.append(update_string)

        update_statement: str = ', '.join(update_params)

        statement = text(f"""UPDATE users SET {update_statement} WHERE id='{user_id}'""")
        self._session.exec(statement)
        self._session.commit()

    def get_user(self, user_id):
        statement = text(f"""SELECT * FROM users WHERE id='{user_id}'""")
        data = self._session.exec(statement).first()
        print(data)

    def delete_user(self, user_id):
        statement = text(f"""DELETE FROM users WHERE id='{user_id}'""")
        self._session.exec(statement)
        self._session.commit()
