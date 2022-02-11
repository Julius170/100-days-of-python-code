# THE TRIVIA API AND THE QUIZZLER APP
from cgitb import text
from tkinter import font
import requests
import html 
from  tkinter import *


THEME_COLOR = "#375362"
class QuizInterface:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("The Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = Label(text= "Score: 0 ", font=("white", 20, "italic"))
        self.label.grid(row=0, column=1)

        canvas =Canvas(text= "", font= ("Ariel", 20, "italic")) 
        
        
        self.window.mainloop


parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get (url="https://opentdb.com/api.php", params=parameters)
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
for questions in question_data:
    question_text = questions["question"]
    question_answer = questions["correct_answer"]
    new_question = Question(question_text, question_answer)
    Question_bank.append(new_question)


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.current_question.text)
        user_answer = input(f"Q{self.question_number}: {question_text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


quiz = QuizBrain(Question_bank)
quiz_ui = QuizInterface()



# while quiz.still_has_question():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


# GUI INTERFACE











