# CREATING A SNAKE GAME
from turtle import Screen, Turtle
import time
import random

# CREATING AND INITIALIZING THE SNAKE OBJECT

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Snake:
    def __init__(self):
        self.oscars = []
        self.create_snake()
        self.head = self.oscars[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_oscar = Turtle("square")
        new_oscar.color("white")
        new_oscar.penup()
        new_oscar.goto(position)
        self.oscars.append(new_oscar)

    def extend(self):
        self.add_segment(self.oscars[-1].position())
        print("Extending")

    def move(self):
        for oscar_num in range(len(STARTING_POSITION) - 1, 0, -1):
            new_x = self.oscars[oscar_num - 1].xcor()
            new_y = self.oscars[oscar_num - 1].ycor()
            self.oscars[oscar_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("Green")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = (random.randint(-280, 280))
        random_y = (random.randint(-280, 280))
        self.goto(random_x, random_y)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # SCREEN INITIALIZATION


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # DETECT COLLISION WITH WALL
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

        # DETECT COLLISION WITH TAIL
        for segment in snake.oscars:
            if segment == snake.head:
                pass
            if snake.head.distance < 10:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()
