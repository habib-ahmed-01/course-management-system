# Enrollment Class
#         Attributes: id, user_id, course_id
#         Methods: enroll_user, unenroll_user, get_enrollments

from sqlmodel import text


class EnrollmentManager:
    def __init__(self, session):
        self._session = session

    def enroll_user(self, user_id: str, course_id: str) -> None:
        statement: text = text(
            f"""INSERT INTO enrollments (user_id, course_id) VALUES ('{user_id}', '{course_id}')""")
        self._session.exec(statement)
        self._session.commit()

    def unenroll_user(self, user_id: str, course_id: str) -> None:
        statement: text = text(f"""DELETE FROM enrollments WHERE user_id = '{user_id}' AND course_id = '{course_id}'""")
        self._session.exec(statement)
        self._session.commit()

    def get_enrollments(self, user_id: str = None, course_id: str = None) -> list:
        if user_id and course_id:
            statement: text = text(f"""SELECT * FROM enrollments where user_id='{user_id}' AND course_id='{course_id}'""")
        elif user_id:
            statement: text = text(f"""SELECT * FROM enrollments where user_id='{user_id}'""")
        elif course_id:
            statement: text = text(f"""SELECT * FROM enrollments where course_id='{course_id}'""")
        else:
            raise AttributeError

        return self._session.exec(statement).all()
