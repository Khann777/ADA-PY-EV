# models/reminder.py

class Reminder:
    def __init__(self, reminder_id, task_id, interval, status):
        self.reminder_id = reminder_id
        self.task_id = task_id
        self.interval = interval
        self.status = status  # Например, active или inactive

    def __repr__(self):
        return f"<Reminder {self.interval} for Task {self.task_id}>"
