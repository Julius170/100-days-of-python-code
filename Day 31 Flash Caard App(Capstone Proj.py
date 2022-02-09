# CAPSTONE PROJECT -- FLASH CARD PROGRAM

from tkinter import *
from turtle import onclick
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:

    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("French_words.csv")
    to_learn = original_data.to_dict(orient="French_word.csv")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}


def next_card():
    global cucrrent_card
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["Engligh"], fill="white")
    canvas.itemconfig(card_background, image=card_background)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("Flashy")

window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_font_img = PhotoImage(file="card_font.png")
card_back_img = PhotoImage(file="card_back.png")
card_background = canvas.create_image(200, 263, img=card_font_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Airel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Airel", 60, "bold"))
canvas.grid(row=0, column=0)

cross_image = PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(row=1, column=0, columnspan=2, hightlightthickness=0)

check_image = PhotoImage(file="right.png")
known_button = Button(image=check_image, command=is_known)
known_button.grid(row=1, column=1, hightlightthickness=0)

next_card()
window.mainloop()

# THIS PROJECT NEEDS THE DAY 31 COURSE RESOURCES TO BE COMPLETE
# FINITE
