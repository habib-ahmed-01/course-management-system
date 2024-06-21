# Methods: create_user, authenticate, update_user, delete_user
from sqlmodel import text
class UserManager:
    def __init__(self, session):
        self._session = session
        self.statement = None

    def create_user(self, username, email, password, role):
        self.statement = text(f"""INSERT INTO users (username, email, password, role) values ('{username}', '{email}', '{password}', '{role}')""")
        self._session.exec(self.statement)
        self._session.commit()
        return True

    def update_user(self, user_id, *kwargs):
        ...