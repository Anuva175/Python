
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'change-this-secret-key'  # For flash messages

db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id} {self.title!r}>"

# READ (List) + optional EDIT mode (same page)
@app.route('/')
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    edit_id = request.args.get('edit', type=int)
    edit_task = Task.query.get(edit_id) if edit_id else None
    return render_template('index.html', tasks=tasks, edit_task=edit_task)

# CREATE
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    if not title:
        flash('Title is required.', 'danger')
        return redirect(url_for('index'))
    task = Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()
    flash('Task added successfully.', 'success')
    return redirect(url_for('index'))

# UPDATE (complete)
@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.status = 'Completed'
    db.session.commit()
    flash('Task marked as Completed.', 'info')
    return redirect(url_for('index'))

# UPDATE (edit title/description/status) — same page
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    status = request.form.get('status', 'Pending')
    if not title:
        flash('Title is required.', 'danger')
        # Stay on the same page in edit mode if validation fails
        return redirect(url_for('index', edit=task.id))
    task.title = title
    task.description = description
    task.status = status
    db.session.commit()
    flash('Task updated successfully.', 'success')
    return redirect(url_for('index'))

# DELETE
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted.', 'warning')
    return redirect(url_for('index'))

# CLI helper (optional)
@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Initialized the database: todo.db')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
