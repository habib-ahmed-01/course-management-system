# Enrollment Class
#         Attributes: id, user_id, course_id
#         Methods: enroll_user, unenroll_user, get_enrollments

class Enrollment:
    def __init__(self, _id: str, user_id: str, course_id: str):
        self.enroll_id: str = _id
        self.user_id: str = user_id
        self.course_id: str = course_id
