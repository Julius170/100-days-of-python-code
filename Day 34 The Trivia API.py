# THE TRIVIA API AND THE QUIZZLER APP

from numpy import False_
import requests
import html
from tkinter import *

THEME_COLOR = "#375362"



class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {question_text}" 

        # user_answer = input(f"Q.{self.question_number}: {question_text} (True/False):")
        # self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            True
        else:
            False
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
# GUI INTERFACE


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.still_has_question():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemcongif(self.questions_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the quiz.")
            self.true_button.config(state="disabled") 
            self.false_button.config(state="disabled") 

    def true_pressed(self):
        is_right = self.give_feedback(self.quiz.check_answer("True")) 
        
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.cofig(bg="red")

        self.window.after(1000, self.get_next_question)




class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        quiz = quiz_brain 

        self.window = Tk()
        self.window.title("The Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = Label(text="Score: 0 ", font=("white", 20, "italic"))
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR, font= ("Ariel", 20, "italic"))
        self.canvas.grid(row=0, column=2, columnspan=2, padx=34)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(true=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command = self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next

        self.window.mainloop()


    parameters = {
    "amount": 10,
    "type": "boolean"
    }

    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()

    data = response.json()
    question_data = data["results"]


# TRUTH OR FALSE GAME


# TODO 1. CREATE A QUESTION CLASS FROM SCRATCH
class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


        Question_bank = []
        for questions in self.question_data:
            question_text = questions["question"]
            question_answer = questions["correct_answer"]
            new_question = Question(question_text, question_answer)
            Question_bank.append(new_question)



quiz = QuizBrain()
quiz_ui = QuizInterface()

# while quiz.still_has_question():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")





# # TYPE HINTS AND  ARROWS
# app: int
# name: str
# height: float
# is_button: bool 

# def police_check(age):
#         if age > 18:
#             can_drive = True
#             return can_drive
#         else:
#             can_drive = False
#             return can_drive


# print(police_check(16))


