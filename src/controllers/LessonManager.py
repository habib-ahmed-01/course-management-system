# Lesson Class
#         Attributes: id, title, content, course_id
#         Methods: create_lesson, update_lesson, delete_lesson, get_lesson

from sqlmodel import text


class LessonManager:
    def __init__(self, session):
        self._session = session

    def create_lesson(self, title: str, content: str, course_id: str) -> None:
        statement: text = text(
            f"""INSERT INTO lessons (title, content, course_id) VALUES ('{title}', '{content}', '{course_id}')""")
        self._session.exec(statement)
        self._session.commit()

    def update_lesson(self, lesson_id: str, **kwargs: str) -> None:
        update_params: list = []
        for key, value in kwargs.items():
            update_string: str = f"{key}='{value}'"
            update_params.append(update_string)

        update_statement: str = ', '.join(update_params)

        statement = text(f"""UPDATE courses SET {update_statement} WHERE id='{lesson_id}'""")
        self._session.exec(statement)
        self._session.commit()

    def get_lesson(self, lesson_id: str) -> tuple:
        statement: text = text(f"""SELECT * FROM lessons WHERE id='{lesson_id}'""")
        return self._session.exec(statement).first()

    def get_all(self) -> list:
        statement: text = text(f"""SELECT * FROM lessons""")
        return self._session.exec(statement).all()

    def delete_lesson(self, lesson_id: str) -> None:
        statement: text = text(f"""DELETE FROM courses WHERE id='{lesson_id}'""")
        self._session.exec(statement)
        self._session.commit()
