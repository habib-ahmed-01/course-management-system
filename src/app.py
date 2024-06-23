from controllers.CourseManager import CourseManager
from controllers.UserManager import UserManager
from controllers.LessonManager import LessonManager
from controllers.EnrollmentManager import EnrollmentManager
from utils.db import database_connection

if __name__ == '__main__':
    session = database_connection('postgresql')
    course = EnrollmentManager(session)
    print(course.enroll_user(user_id="8308dc90-1897-4bd4-b4be-5a7d59350a85", course_id='90b0aebe-7c34-4909-9889'
                                                                                       '-d002729b93df'))
