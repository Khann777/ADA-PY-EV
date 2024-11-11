# handlers/task_handler.py

from controllers.task_controller import TaskController

class TaskHandler:
    def __init__(self, task_controller=None):
        self.task_controller = task_controller or TaskController()

    def handle_create_task(self, message):
        # Логика создания задачи
        pass

    def handle_edit_task(self, message):
        # Логика редактирования задачи
        pass

    def handle_delete_task(self, message):
        # Логика удаления задачи
        pass
