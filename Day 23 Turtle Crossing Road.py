from turtle import Turtle, Screen
import time
import random

# PLAYER START
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            False


# PLAYER ENDS


# CAR MANAGER STARTS
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
    #         # CAR MANAGER ENDS


MOVE_INCREMENT = 10

# SCOREBOARD STARTS


FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-250, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)



# SCOREBOARD ENDS


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    # DETECT TURTLE COLLISION WITH CAR
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        # DETECTING A COMPLETE CROSSING
        if player.is_at_finish():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()

screen.exitonclick()
