# Methods: create_user, authenticate, update_user, delete_user
from sqlmodel import text


class UserManager:
    def __init__(self, session):
        self._session = session

    def create_user(self, username: str, email: str, password: str, role: str):
        statement: text = text(
            f"""INSERT INTO users (username, email, password, role) values ('{username}', '{email}', '{password}', '{role}')""")
        self._session.exec(statement)
        self._session.commit()

    def update_user(self, user_id: str, **kwargs: str):
        update_params: list = []

        for key, value in kwargs.items():
            update_string: str = f"{key}='{value}'"
            update_params.append(update_string)

        update_statement: str = ', '.join(update_params)

        statement = text(f"""UPDATE users SET {update_statement} WHERE id='{user_id}'""")
        self._session.exec(statement)
        self._session.commit()

    def delete_user(self, user_id):
        statement = text(f"""DELETE FROM users WHERE id='{user_id}'""")
        self._session.exec(statement)
        self._session.commit()
