# Flask Task Manager (CRUD)

A small full-stack app built with Flask, SQLAlchemy, and SQLite.
It has a web UI and a JSON REST API for the same data.

## Run it
```bash
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Features
- Create, read, update, and delete tasks
- Mark tasks done or reopen them
- REST API with JSON responses

## API
| Method | Endpoint | Action |
|--------|----------|--------|
| GET | /api/tasks | List all tasks |
| GET | /api/tasks/<id> | Get one task |
| POST | /api/tasks | Create (`{"title": "...", "description": "..."}`) |
| PUT | /api/tasks/<id> | Update |
| DELETE | /api/tasks/<id> | Delete |

## Stack
Python, Flask, Flask-SQLAlchemy, SQLite, Jinja2, HTML, CSS
