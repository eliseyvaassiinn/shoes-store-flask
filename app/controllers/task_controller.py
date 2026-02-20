# app/controllers/task_controller.py

from flask import render_template, request, redirect, url_for, flash

from app.models.task import TaskModel

class TaskController:
    def __init__(self):
        self.model = TaskModel()

    def index(self):
        tasks = self.model.get_all_tasks()
        return render_template('tasks/index.html', tasks=tasks)

    def store(self):
        description = request.form.get('description', '').strip()
        if not description:
            flash('Опис не може бути порожнім!', 'error')
            return redirect(url_for('index'))  

        if self.model.add_task(description):
            flash('Завдання додано!', 'success')
        else:
            flash('Не вдалося додати завдання', 'error')

        return redirect(url_for('index'))            

    def mark_done(self, task_id: int):
        if self.model.mark_done(task_id):
            flash('Завдання позначено як виконане!', 'success')
        else:
            flash('Завдання не знайдено', 'error')
        return redirect(url_for('index'))         

    def delete(self, task_id: int):
        self.model.delete_task(task_id)
        flash('Завдання видалено!', 'success')
        return redirect(url_for('index'))         