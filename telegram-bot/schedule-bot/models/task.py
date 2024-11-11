# models/task.py

class Task:
    def __init__(self, task_id, title, description, deadline, priority, status, user_id):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.status = status
        self.user_id = user_id

    def __repr__(self):
        return f"<Task {self.title}, Deadline: {self.deadline}, Priority: {self.priority}>"
