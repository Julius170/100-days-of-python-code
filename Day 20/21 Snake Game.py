# CREATING A SNAKE GAME

from turtle import Screen, Turtle
import time
import random


# CREATING AND INITIALIZIN THE SNAKE OBJECT

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20 
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.oscars = []
        self.create_snake()
        self.head = self.oscars[0]
        
    def create_snake(self):
        for position in STARTING_POSITION:
            new_oscar = Turtle("square")
            new_oscar.color("white")
            new_oscar.penup()
            new_oscar.goto(position)
            self.oscars.append(new_oscar)
            
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
        self.write
        
        
        
    def refresh(self):
        random_x = (random.randint(-280, 280))        
        random_y = (random.randint(-280, 280))        
        self.goto(random_x, random_y)
    
        
        
        
        
          
        
        
        
        
        
# SCREEN INITIALIZATION
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()

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
        

screen.exitonclick()



















