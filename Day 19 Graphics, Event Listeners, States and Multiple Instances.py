# MORE TURTLE GRAPHICS, EVENT LISTENER, STATE AND MULTIPLE INSTANCES
from turtle import Turtle, Screen
import random

# oscar = Turtle()
# screen = Screen()


# # EVENT LISTENER
# def move_forwards():
#     oscar.forward(10)
# def move_back():
#     oscar.back(10)
#     # MY SOLUTION
# # def move_left():
# #     oscar.left(90)
# #     oscar.forward(10)
# # def move_right():
# #     oscar.right(90)
# #     oscar.forward(10)
# def clear():
#     oscar.clear()
#     oscar.penup()
#     oscar.home()
#     oscar.pendown()

# # COURSES SOLUTION
# def turn_right():
#     new_heading = oscar.heading() + 10
#     oscar.setheading(new_heading)
# def turn_left():
#     new_heading = oscar.heading() - 10
#     oscar.seetheading(new_heading)
# screen.listen()     # LISTENS FOR EVENTS TO TAKE ACTIONS
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")


# BUILDING A TURTLE RACE


# is_race_on = False
# screen = Screen()
# screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# y_positioning = [-70, -40, -10, 20, 50, 80]
# all_turtles = []

# for turtle_index in range(0, 6):
#     new_turtle = Turtle(shape="turtle")
#     new_turtle.color(colors[turtle_index])
#     new_turtle.penup()
#     new_turtle.goto(x=-230, y=y_positioning[turtle_index])
#     all_turtles.append(new_turtle)

# if user_bet:
#     is_race_on = True

# while is_race_on:
#     for turtle in all_turtles:
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You've Won!, The {winning_color} turtle is the winner!")
#             else:
#                 print(f"You lose!, The {winning_color} turtle is the winner!")
#             rand_distance = random.randint(0, 10)
#             turtle.forward(rand_distance)

# screen.exitonclick()

# FINITE
