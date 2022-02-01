# import pandas
# with open("day 25 weather_data_csv.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
# with open("day 25 weather_data_csv.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temp = []
#     for rows in data:
#         if rows[1] != "temp":
#             temp.append(int(rows[1]))
#     print(temp)


# data = pandas.read_csv("day 25 weather_data_csv.csv")

# print(type(data))
# print(data)

# data_dict = data.to_dict()
# print(data_dict)

# CHECK OUT "pandas.datatypes.org/docs" FOR DOCUMENTATIONS ON PANDAS
# temp_list = data["temp"].to_list()

# print(int(data["temp"].mean()))

# print(data["temp"].max())

# print(temp_list)

# GETTING DATA IN COLUMNS
# print(data["condition"])

# print(data.day)

# GETTING DATA IN ROWS
# print(data[data.day == "Monday"])
# monday = (data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)

# monday_temp_f = monday_temp * 9/5 + 32

# print(monday_temp_f)


# # CREATING A DATAFRAME FROM SCRATCH
# data_dict = {
#     "students": ["Sunshine", "Olamide", "Phensic"],
#     "scores": [76, 54, 45]
# }

#
# data = pandas.DataFrame(data_dict)
#
# print(data)
# data.to_csv("new_data.csv")


# SQUIRREL COUNT CHALLENGE

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_fur_count = len(data[data["Primary Fur Color"] == "Gray"])
# black_fur_count = len(data[data["Primary Fur Color"] == "Black"])
# red_fur_count = len(data[data["Primary Fur Color"] == "Cinnamon"])


# print(black_fur_count)
# print(gray_fur_count)
# print(red_fur_count)

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_fur_count, red_fur_count, black_fur_count]
#     }


# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel.csv")

# THE 50 U.S. GUESSING GAME 

import turtle
from turtle import Screen, textinput
import pandas


screen = Screen()
screen.screensize()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
guessed_states = []



while len(guessed_states) < 50:
        
    answer_state = textinput(title = f"{len(guessed_states)}/50 States Correct", prompt ="What's another state name?" ).title()

    #  MY INCOMPLETE SOLUTION
    # CHECKS IF THE USERS ANSWER IS ONE OF THE LIST OF THE 50 STATES
    # for states in data["state"]:
    #     if answer_state == states:
    #         print(answer_state)
        #     t = turtle.Turtle()
        #     t.hideturtle()
        #     t.penup()
        #     correct_ans = data[data.state == answer_state]
        #     cor_x = int(correct_ans.x)
        #     cor_y = int(correct_ans.y)
        #     t.goto(cor_x, cor_y)
        #     t.write(answer_state)

    # COURSES SOLUTION
    all_state = data.state.to_list()


    if answer_state == "Exit":
        # DAY 26 MODIFICATION 
        missing_states = [states for states in all_state if states != guessed_states]
        
        # PREVIOUS SOLUTION
        # for states in all_state:
        #     if states not in all_state:
                # missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] 
        t.goto(int(state_data.x), int(state_data.x))
        t.write(answer_state)




screen.exitonclick()

