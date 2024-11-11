# controllers/task_controller.py
from models.task import Task
from services.db_service import DBService  # Внедрение зависимости для работы с БД

class TaskController:
    def __init__(self, db_service=None):
        self.db_service = db_service or DBService()  # Внедрение зависимости

    def create_task(self, user_id, title, description, deadline, priority):
        task = Task(None, title, description, deadline, priority, 'pending', user_id)
        self.db_service.add_task(task)
        return task

    def edit_task(self, task_id, title=None, description=None, deadline=None, priority=None):
        task = self.db_service.get_task_by_id(task_id)
        if title:
            task.title = title
        if description:
            task.description = description
        if deadline:
            task.deadline = deadline
        if priority:
            task.priority = priority
        self.db_service.update_task(task)
        return task

    def delete_task(self, task_id):
        self.db_service.delete_task(task_id)
