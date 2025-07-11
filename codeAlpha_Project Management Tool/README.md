# Project Management Tool – CodeAlpha Internship (Task 3)

This is a simple Django-based project manager web app built for the CodeAlpha Full Stack Web Development Internship.

## Features
- View all projects
- Add tasks to a project
- List all tasks under a project

## Tech Stack
- Python
- Django
- HTML, CSS

## How to Run
```bash
pip install django
django-admin startproject project_manager
cd project_manager
python manage.py startapp dashboard
# Replace files with those in this repo
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
