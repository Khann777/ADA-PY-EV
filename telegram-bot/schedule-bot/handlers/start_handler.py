from services.db_service import get_user
from services.notification_service import send_notification

# Хендлер для команды /start
def start(message):
    user_id = message.from_user.id
    user = get_user(user_id)
    
    if not user:
        send_notification(user_id, "Добро пожаловать! Пожалуйста, зарегистрируйтесь.")
    else:
        send_notification(user_id, f"Привет, {user.first_name}!")
