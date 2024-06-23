# Course Management System

A Course Management System written in Python, designed to be user-friendly and easily configurable. The system allows managing courses, users, lessons, and enrollments with database connectivity via SQLModel.

## Features

- **Core Functionality**: Manage courses, users, lessons, and enrollments.
- **Database Connectivity**: Connect to any SQL database using SQLModel.
- **Modular Design**: Separate models and controllers for better organization and maintenance.
- **Easy Configuration**: Configure database settings through a `secrets.toml` file.

## Folder Structure

src/
├── controllers/
│ ├── CourseManager.py
│ ├── EnrollmentManager.py
│ ├── LessonManager.py
│ └── UserManager.py
├── models/
│ ├── Course.py
│ ├── Enrollment.py
│ ├── Lesson.py
│ └── User.py
├── utils/
│ └── db.py
├── app.py
└── secrets.toml


## Getting Started

### Prerequisites

- Python 3.7 or higher
- SQLModel

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/course-management-system.git
    ```

2. Navigate to the project directory:
    ```sh
    cd course-management-system/src
    ```

3. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1. Create a `secrets.toml` file in the `src` directory with the following content:
    ```toml
    [postgresql]
    dialect = "postgresql"
    host = "localhost"
    port = "5432"
    database = "course_management"
    username = "postgres"
    password = "password123#"  # Replace with your database deets
    ```

2. Update the `secrets.toml` file with your database details.

### Running the Application

1. Ensure you are in the `src` directory and your virtual environment is activated.

2. Run the application:
    ```sh
    python app.py
    ```

## Usage

### Models

The project includes four primary models:
- `Course`
- `User`
- `Lesson`
- `Enrollment`

### Controllers

The functionality to add, create, delete, or get details for each model is managed by their respective controllers:
- `CourseManager.py`
- `UserManager.py`
- `LessonManager.py`
- `EnrollmentManager.py`

### Example Usage in `app.py`

Import the necessary managers and use their functions as needed:
```python
from controllers.coursemanager import CourseManager
from controllers.usermanager import UserManager
from controllers.lessonmanager import LessonManager
from controllers.enrollmentmanager import EnrollmentManager

# Example usage
CourseManager.create_course(...)
UserManager.add_user(...)
LessonManager.create_lesson(...)
EnrollmentManager.enroll_user(...)


## Acknowledgements

- [SQLModel](https://sqlmodel.tiangolo.com/)

