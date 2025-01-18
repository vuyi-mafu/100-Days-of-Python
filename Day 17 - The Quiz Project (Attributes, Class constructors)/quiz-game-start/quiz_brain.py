class QuizBrain:

    def __init__(self, question_bank):

        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {item.text} (True/False): ")

        self.check_answer(answer, item.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def still_has_questions(self):
        list_length = len(self.question_list)
        if list_length > self.question_number:
            self.question_number += 1
            return True
        else:
            return False

