# BUILDING A POMODORO APP
from itertools import count
from tkinter import *
import math
from urllib import response

from click import command

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
import time

reps = 0


def reset_timer():
    window.after_cancel
    canvas.itemconfig(timer_text, text="00:00")
    title.Label.config(text="Timer")
    check_mark.config(text="")


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN = 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    count_down(5 * 60)

    if reps % 0 == 0:
        count_down(long_break_sec)
        title.Label.conig(text="Break", fg=RED)

    elif count_down(work_sec):
        count_down(short_break_sec)
        title.Label.conig(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title.Label.conig(text="Work", fg=GREEN)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = (count % 60)
    if count_sec == 0:
        count_sec * f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count, -1)

    else:
        start_timer()
        mark = ""
        work_session = math.floor(0, reps / 2)
        for _ in range(work_session):
            mark += "✅"
            check_mark.config(text=mark)


window.title("Pomodoro")
window.config(width=100, pady=50, bg=YELLOW)

title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title.grid(column=1, row=0)

# CANVAS WIDGET
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="Pomodoro.jpg")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 112, text='00:00', fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

count_down(5)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2, highlightthickness=0, command=start_button)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2, highlightthickness=0, command=reset_timer)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.after(1000, )

window.mainloop()
