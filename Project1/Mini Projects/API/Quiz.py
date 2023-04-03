import requests
import html

response = requests.get('https://opentdb.com/api.php?amount=10&category=17&difficulty=medium&type=boolean')
response.raise_for_status()
data = response.json()

question_data = data['results']


class Question:

    def __init__(self,qtext, qanswer):
        self.text = qtext
        self.answer = qanswer


class QuizBrain:

    def __init__(self,qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        user_answer = input(f'Q.{self.question_number}: {q_text} (True/False):')
        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        if user_answer.lower() == self.current_question.answer.lower():
            self.score += 1
            print(f'You got it right! Your corrunt score is {self.score}')
        else:
            print(f'That\'s wrong! The correct answer is {self.current_question.answer}')


question_bank = []

for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(qtext=question_text,qanswer=question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f'result: {quiz.score}/{len(question_bank)}')