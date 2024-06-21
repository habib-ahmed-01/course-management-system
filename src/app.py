from controllers.CourseManager import CourseManager
from controllers.UserManager import UserManager
from utils.db import database_connection

if __name__ == '__main__':
    session = database_connection('postgresql')
    course = CourseManager(session)
    print(course.create_course(title="Mathematics", description="Engineering Mathematics", instructor_id='8308dc90-1897-4bd4-b4be-5a7d59350a85'))
