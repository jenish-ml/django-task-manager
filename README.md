# Django Task Manager

This repository contains a Task Manager application built using the Django framework. The application allows users to manage tasks efficiently with functionalities to add, edit, delete, and view tasks. Users can also filter tasks by priority levels. The application includes a command-line interface (CLI) for task management.

## Key Features

- Add tasks with title, description, priority (High/Medium/Low), and status (Pending/In Progress/Completed)
- Edit existing tasks
- Delete tasks
- View all tasks with their details
- Filter tasks by priority
- Command-line interface (CLI) for managing tasks

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x or later

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/django-task-manager.git
    cd django-task-manager
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin interface:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the Django development server:
    ```sh
    python manage.py runserver
    ```

7. Access the Django admin interface at `http://127.0.0.1:8000/admin/` to manage tasks.

### Using the CLI

The Task Manager application provides a command-line interface (CLI) for managing tasks. To use the CLI, run the following command:

```sh
python manage.py manage_tasks
