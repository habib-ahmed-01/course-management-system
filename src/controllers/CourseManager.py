# Course Class
#         Attributes: id, title, description, instructor_id
#         Methods: create_course, update_course, delete_course, get_course

from sqlmodel import text


class CourseManager:
    def __init__(self, session):
        self._session = session

    def create_course(self, title: str, description: str, instructor_id: str) -> None:
        statement: text = text(
            f"""INSERT INTO courses (title, description, instructor_id) values ('{title}', '{description}', '{instructor_id}')""")
        self._session.exec(statement)
        self._session.commit()

    def update_course(self, course_id: str, **kwargs: str) -> None:
        update_params: list = []
        for key, value in kwargs.items():
            update_string: str = f"{key}='{value}'"
            update_params.append(update_string)

        update_statement: str = ', '.join(update_params)

        statement = text(f"""UPDATE courses SET {update_statement} WHERE id='{course_id}'""")
        self._session.exec(statement)
        self._session.commit()

    def get_course(self, course_id: str) -> tuple:
        statement: text = text(f"""SELECT * FROM courses WHERE id='{course_id}'""")
        return self._session.exec(statement).first()

    def get_all(self) -> list:
        statement: text = text(f"""SELECT * FROM courses""")
        return self._session.exec(statement).all()

    def delete_course(self, course_id: str) -> None:
        statement: text = text(f"""DELETE FROM courses WHERE id='{course_id}'""")
        self._session.exec(statement)
        self._session.commit()
