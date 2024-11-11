import telebot
from config import TELEGRAM_API_TOKEN
from handlers.start_handler import start
from handlers.task_handler import handle_task_commands
from handlers.reminder_handler import handle_reminder_commands

# Инициализация бота с использованием токена
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

# Установка хендлеров команд
bot.message_handler(commands=['start'])(start)
bot.message_handler(commands=['newtask', 'edittask', 'deletetask', 'alltasks'])(handle_task_commands)
bot.message_handler(commands=['setreminder', 'reminders'])(handle_reminder_commands)

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
