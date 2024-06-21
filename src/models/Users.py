# User Class
#         Attributes: id, username, email, password, role
#         Methods: create_user, authenticate, update_user, delete_user

class User:
    def __init__(self, _id, username, email, password, role):
        self.user_id: str = _id
        self.username: str = username
        self.email: str = email
        self.password: str = password
        self.role: str = role
