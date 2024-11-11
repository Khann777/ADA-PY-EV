import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

# Функция для создания соединения с базой данных
def create_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

# Пример функции для добавления задачи в базу данных
def add_task(task):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (title, description, deadline, priority, status, user_id) VALUES (%s, %s, %s, %s, %s, %s)",
        (task.title, task.description, task.deadline, task.priority, task.status, task.user_id)
    )
    conn.commit()
    cur.close()
    conn.close()

# services/db_service.py

class DBService:
    def __init__(self, db_connection):
        self.db_connection = db_connection  # Внедрение зависимости для подключения к БД

    def add_task(self, task):
        """Добавляем задачу в базу данных"""
        # Пример кода, сохраняющего задачу в БД
        pass

    def get_task_by_id(self, task_id):
        """Получаем задачу по ID"""
        pass

    def update_task(self, task):
        """Обновляем задачу в БД"""
        pass

    def delete_task(self, task_id):
        """Удаляем задачу из БД"""
        pass

    def save_user(self, user):
        """Сохраняем пользователя в БД"""
        pass
