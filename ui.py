THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 145, text="hello", width=280, font=("Arial", 30, "italic"), fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        false_image = PhotoImage(file="images/false.png")
        self.button = Button(image=false_image, highlightthickness=0, command=self.false_preseed)
        self.button.grid(row=2, column=0)
        true_image = PhotoImage(file="images/true.png")
        self.button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.button.grid(row=2, column=1)
        self.get_next()
        self.window.mainloop()

    def get_next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="you have reached end of the game")
            self.true_pressed.config(state="disabled")
            self.false_preseed.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_preseed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next)