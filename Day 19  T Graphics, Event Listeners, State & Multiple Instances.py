# MORE TURTLE GRAPHICS, EVENT LISTENER, STATE AND MULTIPLE INSTANCES
from turtle import Turtle, Screen

oscar = Turtle()
screen = Screen()


def move_forwards():
    oscar.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()

# EVENT LISTENER
