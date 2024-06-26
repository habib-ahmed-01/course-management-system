# Course Class
#         Attributes: id, title, description, instructor_id
#         Methods: create_course, update_course, delete_course, get_course

class Course:
    def __init__(self, _id: str, title: str, description: str, instructor_id: str):
        self.course_id: str = _id
        self.title: str = title
        self.description: str = description
        self.instructor_id: str = instructor_id
