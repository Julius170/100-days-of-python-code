# from turtle import Turtle, Screen
# import random

# TODO 1 CHALLENGE 1
# oscar = Turtle()


# oscar.shape("turtle")
# oscar.color("blue")

# for _ in range(4):
#     oscar.forward(100)
#     oscar.right(90)

#  BASIC IMPORT

# import turtle
# oscar = turtle.Turtle()
# or
# from turtle import Turtle
# or
# from turtle import *
# from random import *


# ALIASING MODULES
# import turtle as t
# tim = t.Turtle()

# for _ in range(10):
#     oscar.forward(10)
#     oscar.penup()
#     oscar.forward(10)
#     oscar.pendown()

# colors = ("red", "green", "blue", "yellow", "violet", "orange", "purple", "indigo")

# DRAWING A TRIANGLE TO A DECAGON
# def draw_shape(side_num):
#     angle = 360 / side_num
#     for _ in range(side_num):
#         oscar.forward(100)
#         oscar.right(angle)


# for shape_side_n in range(3, 11):
#     oscar.color(random.choice(colors))
#     draw_shape(shape_side_n)

# CREATING A RANDOM TURTLE MOVEMENT

# direction = [0, 90, 180, 270, 360]
# oscar.pensize(15)
# oscar.speed("fastest")
# oscar.colormode(255)

# CREATING A RANDOM COLOR GENERATOR FOR THE TURTLE
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color


# for _ in range(200):
#     oscar.color(random_color())
#     oscar.color(random.choice(colors))
#     oscar.forward(20)
#     oscar.setheading(random.choice(direction))

# CREATING A SPIROGRAPH
# oscar.speed("fastest")

# def draw_spiro(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         oscar.color(random_color())
#         oscar.circle(100)
#         oscar.setheading(oscar.heading() + 10)
#         oscar.circle(100)

# draw_spiro(5)


# CREATING AN IMAGE COLOR EXTRACTOR

# import colorgram
# rgb_colors = []
# colors = colorgram.extract("hisrt's_image.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# REPLICATING HIRST'S PAINTING

import turtle as turtle_module
import random

turtle_module.colormode(255)
oscar = turtle_module.Turtle()
oscar.speed("fastest")
oscar.hideturtle()
oscar.penup()
color_list = [(192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123),
              (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26),
              (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127), (177, 188, 215), (164, 104, 134),
              (115, 31, 46), (97, 150, 100), (98, 121, 172), (210, 178, 197), (174, 105, 93), (74, 150, 165),
              (25, 91, 65), (172, 205, 180)]

oscar.setheading(225)
oscar.forward(300)
oscar.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    oscar.dot(15, random.choice(color_list))
    oscar.forward(50)

    if dot_count % 10 == 0:
        oscar.setheading(90)
        oscar.forward(50)
        oscar.setheading(180)
        oscar.forward(500)
        oscar.setheading(0)

print(oscar)

screen = turtle_module.Screen()
screen.exitonclick()

# FINITE