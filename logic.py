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
    Question("2+2?", ["3", "4", "5"], "4"),
    Question("Столица Франции?", ["Париж", "Лондон", "Берлин"], "Париж"),
]


class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def check_answer(self, user, answer):
        correct = self.questions[user.current_question].correct
        return answer == correct


quiz = Quiz(questions)
