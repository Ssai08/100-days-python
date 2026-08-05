from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question = QuestionModel(i["question"],i["correct_answer"])
    question_bank.append(question)

# print(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You have completed the quiz.\nYour final score is {quiz.score}/{quiz.question_number}.")