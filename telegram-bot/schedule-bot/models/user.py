# models/user.py

class User:
    def __init__(self, user_id, first_name, last_name=None, premium=False, db_service=None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.premium = premium
        self.db_service = db_service  # Внедрение зависимости для работы с БД
    
    def save(self):
        """Сохраняем данные пользователя в базу данных"""
        if self.db_service:
            self.db_service.save_user(self)

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}, ID={self.user_id}>"
