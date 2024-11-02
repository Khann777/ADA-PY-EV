import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

"""
Декоратор message_handler нужен, чтобы реагировать на определенные сообщения
Этот декоратор принимает commands - список команд (функция работает, когда пользователь написал одну из них)

content_types - список типов сообщений (text, audio, document, photo, sticker, video, video_note, voice, location, contact, new_chat_members, left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo, group_chat_created, supergroup_chat_created, channel_chat_created, migrate_to_chat_id, migrate_from_chat_id, pinned_message, web_app_data)

content_types=['text'] - функция будет работать, когда пользователь отправит в чат любое текстовое сообщение
content_types=['audio'] - функция будет работать, когда пользователь отправит в чат любое аудио сообщение
"""

#* Клавиатура, которая находится там, где клавиатура
keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Да')
button2 = telebot.types.KeyboardButton('Нет')
keyboard.add(button1, button2)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text='Привет, выбери кнопку!', reply_markup=keyboard)

    #* register_next_step_handler() - принимает сообщение и функцию, которая вызовется как только пользователь отправит любое сообщение, это сообщение и передается в функцию
    bot.register_next_step_handler(message, reply_to_button)

def reply_to_button(message):
    if message.text == 'Да':
        bot.send_message(message.chat.id, 'Молодец!')
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, 'Ок')
    else:
        bot.send_message(message.chat.id, 'Нажми на кнопку!')
        bot.register_next_step_handler(message, reply_to_button)



#* @bot.message_handler(commands=['start', 'hello'])
#* def start_message(message):
#*     print(message)
#*     bot.send_message(message.chat.id, 'Привет') # Отправляет сообщение "Привет" в указанный чат (id чата берется из message, который принимает функция) 

bot.polling()