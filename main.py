import telebot
from telebot import types
from logic import *
from config import TOKEN
from db import DB_Manager

bot = telebot.TeleBot(TOKEN)
users = {}

db = DB_Manager("quiz.db")
db.create_table()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет, я бот-квиз! \n/start_quiz — начать квиз\n/score — посмотреть общий счёт"
    )

@bot.message_handler(commands=['score'])
def score(message):
    user_id = message.chat.id
    total = db.get_score(user_id)

    bot.send_message(user_id, f"Всего правильных ответов: {total}")


@bot.message_handler(commands=['start_quiz'])
def start_quiz(message):
    user_id = message.chat.id

    users[user_id] = User()

    bot.send_message(user_id, "Начинаем квиз!")
    send_question(user_id)


def send_question(user_id):
    user = users[user_id]
    question = questions[user.current_question]

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for option in question.options:
        markup.add(option)

    bot.send_message(user_id, question.text, reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    user_id = message.chat.id

    # ❗ игнорируем команды
    if message.text.startswith("/"):
        return

    # ❗ если не начал игру
    if user_id not in users:
        bot.send_message(user_id, "Сначала напиши /start_quiz")
        return

    user = users[user_id]

    # ❗ защита от ошибки (квиз закончился)
    if user.current_question >= len(questions):
        return

    answer = message.text

    # ✅ проверка ответа (без учёта регистра)
    if quiz.check_answer(user, answer):
        user.score += 1
        db.add_point(user_id)
        bot.send_message(user_id, "✅ Правильно!")
    else:
        bot.send_message(user_id, "❌ Неправильно!")

    user.current_question += 1

    # 🔄 следующий вопрос или конец
    if user.current_question < len(questions):
        send_question(user_id)
    else:
        from telebot.types import ReplyKeyboardRemove

        bot.send_message(
            user_id,
            f"Квиз окончен!\nТвои очки: {user.score}",
            reply_markup=ReplyKeyboardRemove()
        )





bot.polling()