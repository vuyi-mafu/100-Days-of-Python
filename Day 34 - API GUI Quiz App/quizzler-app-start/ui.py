from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        #   Score Label
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        #   Canvas
        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="This is a test",
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR)

        self.canvas.grid(row=1, columnspan=2, padx=50, pady=50)

        #   Buttons
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        self.true_button = Button()
        self.true_button.config(image=self.true_image, command=self.true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button()
        self.false_button.config(image=self.false_image, command=self.false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz.\nYour final score is "
                                                            f"{self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self):
        is_right = self.quiz.check_answer("True")
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.give_feedback(is_right)

    def false(self):
        is_right = self.quiz.check_answer("False")
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.window.after(1000, self.get_next_question)
