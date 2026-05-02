class User:
    def __init__(self):
        self.score = 0
        self.current_question = 0


class Question:
    def __init__(self, text, options, correct):
        self.text = text
        self.options = options
        self.correct = correct


questions = [
    Question(
        "Что такое GIL в Python?",
        [
            "Глобальная блокировка интерпретатора",
            "Общий язык интерфейса",
            "Уровень графического ввода"
        ],
        "Глобальная блокировка интерпретатора"
    ),

    Question(
        "Какая функция используется для создания декоратора?",
        [
            "@property",
            "@classmethod",
            "Любая функция, принимающая функцию"
        ],
        "Любая функция, принимающая функцию"
    ),

    Question(
        "Как называется метод __init__?",
        [
            "Конструктор",
            "Деструктор",
            "Инициализатор"
        ],
        "Инициализатор"
    ),

    Question(
        "В каком году был создан Python?",
        [
            "2006",
            "2004",
            "1991"
        ],
        "1991"
    )
]


class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def check_answer(self, user, answer):
        correct = self.questions[user.current_question].correct
        return answer.lower() == correct.lower()


quiz = Quiz(questions)