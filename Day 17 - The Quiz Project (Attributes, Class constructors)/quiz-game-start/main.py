from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

# print(question_bank)
# print(len(question_bank))

quiz = QuizBrain(question_bank)
game_on = QuizBrain(question_bank)


while game_on.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz\nYour final score was: {quiz.score}/{len(question_bank)}")
