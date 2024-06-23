# Lesson Class
#         Attributes: id, title, content, course_id
#         Methods: create_lesson, update_lesson, delete_lesson, get_lesson

class Lesson:
    def __init__(self, _id: str, title: str, content: str, course_id: str):
        self.lesson_id: str = _id
        self.title: str = title
        self.content: str = content
        self.course_id: str = course_id
