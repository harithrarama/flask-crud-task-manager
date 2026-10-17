from datetime import datetime

from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, default="")
    done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "created_at": self.created_at.isoformat(),
        }


# ---------- Web pages (CRUD) ----------

@app.route("/")
def index():  # READ all
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():  # CREATE
    title = request.form.get("title", "").strip()
    if title:
        db.session.add(Task(title=title, description=request.form.get("description", "").strip()))
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):  # UPDATE
    task = db.get_or_404(Task, task_id)
    if request.method == "POST":
        task.title = request.form.get("title", task.title).strip() or task.title
        task.description = request.form.get("description", "").strip()
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", task=task)


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle(task_id):
    task = db.get_or_404(Task, task_id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):  # DELETE
    db.session.delete(db.get_or_404(Task, task_id))
    db.session.commit()
    return redirect(url_for("index"))


# ---------- REST API (JSON) ----------

@app.get("/api/tasks")
def api_list():
    return jsonify([t.to_dict() for t in Task.query.order_by(Task.id).all()])


@app.get("/api/tasks/<int:task_id>")
def api_get(task_id):
    return jsonify(db.get_or_404(Task, task_id).to_dict())


@app.post("/api/tasks")
def api_create():
    data = request.get_json(silent=True) or {}
    if not data.get("title"):
        return jsonify(error="title is required"), 400
    task = Task(title=data["title"], description=data.get("description", ""))
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201


@app.put("/api/tasks/<int:task_id>")
def api_update(task_id):
    task = db.get_or_404(Task, task_id)
    data = request.get_json(silent=True) or {}
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.done = data.get("done", task.done)
    db.session.commit()
    return jsonify(task.to_dict())


@app.delete("/api/tasks/<int:task_id>")
def api_delete(task_id):
    db.session.delete(db.get_or_404(Task, task_id))
    db.session.commit()
    return "", 204


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
