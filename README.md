# To-Do List Application

A simple yet functional To-Do List application built with Django. This application allows users to register, log in, and manage their tasks. Each user can create, view, mark as complete, and delete their tasks.

## Features

### User Authentication
- **Registration:**
  - Users can register with a username, email, and password.
  - Password confirmation is required.
  - Redirects to the login page upon successful registration.
- **Login:**
  - Users can log in with their username and password.
  - Redirects to the personalized task list page upon successful login.
- **Logout:**
  - Users can log out and will be redirected to the login page.

### Task Management
- **Task Creation:**
  - Authenticated users can create new tasks with a title.
  - Tasks are associated with the creating user.
- **Task Display:**
  - Displays a list of tasks for the logged-in user.
  - Tasks are shown with their title, creation time, and completion status.
  - Pagination is implemented for long task lists.
- **Task Completion:**
  - Users can mark tasks as completed using a "Complete" button.
- **Task Deletion:**
  - Users can delete tasks using a "Delete" button.

### User Interface
- **Header:**
  - Includes links to registration, login, and logout pages.
- **Error Handling:**
  - Custom 404 error page for handling "page not found" errors.

## Technical Stack
- **Frontend:**
  - HTML and CSS for structure and styling.
  - Forms for user registration, login, and task management.
- **Backend:**
  - Django web framework.
  - Django ORM for database interactions.
  - Built-in Django authentication system.
  - MySQL as the database backend.

## Deployment
The application can be deployed on a web hosting service like PythonAnywhere. Configuration for static files, database settings, and web server gateway interface (WSGI) is handled according to hosting requirements.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/todolist.git
    cd todolist
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Visit the application:**
    Open a web browser and go to `http://127.0.0.1:8000`.

## Configuration for Deployment

1. **Static Files:**
    - Ensure `STATIC_ROOT` is set in `settings.py`.
    - Run `python manage.py collectstatic`.

2. **Database Configuration:**
    - Configure the database settings in `settings.py` for the production database.

3. **WSGI Configuration:**
    - Ensure the WSGI configuration file is set correctly for the hosting provider.

4. **Environment Variables:**
    - Set environment variables for secret keys and database credentials securely.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [PythonAnywhere](https://www.pythonanywhere.com/)

