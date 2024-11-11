# controllers/user_controller.py

class UserController:
    def __init__(self, db_service=None):
        self.db_service = db_service or DBService()  # Внедрение зависимости

    def create_user(self, user_id, first_name, last_name=None, premium=False):
        user = User(user_id, first_name, last_name, premium)
        self.db_service.save_user(user)
        return user
