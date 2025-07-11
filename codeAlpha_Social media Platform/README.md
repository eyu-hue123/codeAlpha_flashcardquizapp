# Simple Social Media Platform – CodeAlpha Internship (Task 2)

This is a basic full-stack social media web app built with Django as part of the CodeAlpha Full Stack Web Development Internship.

## Features
- Submit a new post
- View all posts

## Tech Stack
- Python
- Django
- HTML, CSS

## How to Run
```bash
pip install django
django-admin startproject socialmedia
cd socialmedia
python manage.py startapp posts
# Replace generated files with this repo's files
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
