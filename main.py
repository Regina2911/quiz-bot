import telebot
from logic import *
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
users = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! 🤖\n/start_quiz — начать квиз"
    )


@bot.message_handler(commands=['start_quiz'])
def start_quiz(message):
    user_id = message.chat.id
    
    users[user_id] = User()
    
    bot.send_message(user_id, "Начинаем квиз!")
    send_question(user_id)


def send_question(user_id):
    user = users[user_id]
    question = questions[user.current_question]
    
    text = question.text + "\n"
    for option in question.options:
        text += option + "\n"
    
    bot.send_message(user_id, text)


@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    user_id = message.chat.id
    
    if user_id not in users:
        bot.send_message(user_id, "Сначала напиши /start_quiz")
        return
    
    user = users[user_id]
    answer = message.text
    
    if quiz.check_answer(user, answer):
        user.score += 1
        bot.send_message(user_id, "✅ Правильно!")
    else:
        bot.send_message(user_id, "❌ Неправильно!")
    
    user.current_question += 1
    
    if user.current_question < len(questions):
        send_question(user_id)
    else:
        bot.send_message(
            user_id,
            f"Квиз окончен!\nТвои очки: {user.score}"
        )


bot.polling()