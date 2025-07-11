# Real-Time Chat App – CodeAlpha Task 4

A WebSocket-based chat app built using Django + Channels for the CodeAlpha Internship.

## Features
- Send/receive messages in real-time
- WebSocket powered with Channels
- Simple and clean interface

## Tech Stack
- Django
- Django Channels
- HTML, CSS, JS
- SQLite

## How to Run
```bash
pip install django channels
django-admin startproject yourproject
cd yourproject
python manage.py startapp chat
# Replace files with this code
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
