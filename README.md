
# Flask Task Manager (CRUD)

A simple full-stack task management application built with Flask, Flask-SQLAlchemy, and SQLite. It includes a web interface and a JSON REST API.

## Features

- Create, read, update, and delete tasks
- Mark tasks as completed or reopen them
- Store tasks in an SQLite database
- REST API with JSON responses
- Web interface for managing tasks

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Jinja2
- HTML and CSS

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/harithrarama/flask-crud-task-manager.git
cd flask-crud-task-manager
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## REST API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/tasks` | List all tasks |
| GET | `/api/tasks/<id>` | Get one task |
| POST | `/api/tasks` | Create a task |
| PUT | `/api/tasks/<id>` | Update a task |
| DELETE | `/api/tasks/<id>` | Delete a task |

### Example JSON for creating a task

```json
{
  "title": "Learn Flask",
  "description": "Practice CRUD operations"
}
```

## License

This project is available for learning and educational purposes.
