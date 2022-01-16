# #  RANDOMIZARION

import random

random_integer = random.randint(1, 10)      #INCLUDES 0 AND 1
print(random_integer)


random_float = random.random()   #DOESN'T INCLUDE 1 AND 0
random_float * 5
print(random_float)



love_score = random.randint(1, 100)
print(f"Your love score is {love_score}%")


#  EXERCISE: HEAD OF TAIL

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)


random_side = random.randint(0, 1)
if random_side == 1:
    print("Head.")
else:
    print("Tails.")


# # PYTHON LISTS=>  IS MUTABLE
states_of_america = ["Ohio", "Hawaii", "Arizona", "Kenses", "Georgia"]
states_of_america[2] = "Pencilvenia"
print(states_of_america[2])


# # APPENDING/ EXTENDING TO THE LIST
states_of_america.append("Nigeria")
states_of_america.extend(["England", "London", "Central City"])

print(states_of_america) 


# EXERCISE: WHO'S PAYING
seed_token = int(input("Create a seed number: \n"))
random.seed(seed_token)

comma_names = input("Give me evrybody's names, seperated by a comma. \n")
names = comma_names.split(", ")

payers_name = names[random.randint(0, len(names)-1)].capitalize()
print(f"{payers_name} is going to buy the meal today")



fruits = ["Strawberries", "Nectarinse", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)


# EXERCISE: TREASURE MAP 

row1 = ["💘","💘","💘"]
row2 = ["💘","💘","💘"]
row3 = ["💘","💘","💘"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where so you want to put your treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
selected_row = (map[vertical-1])
selected_row [horizontal-1] = "X"

print(f"{row1}\n{row2}\n{row3}")


# EXERCISE: ROCK,  PAPER,  SCISSORS
# MY SOLUITON


player = int(input("What do you choose?, Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

# DETERMINING THE USERS INPUT
if player == 0:
    player = "Rock"
    print(f"You chose {player}.")
elif player == 1:
    player ="Paper"
    print(f"You chose {player}.")
elif player == 2:
    player = "Scissors"
    print(f"You chose {player}.")

# DETERMINING THE COMPUTERS INPUT
    computer = random.randint(0, 2)
    if computer == 0:
        computer = "Rock"
        print(f"The computer chose {computer}.")
    elif computer == 1:
        computer = "Paper"
        print(f"The computer chose {computer}.")
    elif computer == 2:
        computer = "Scissors"
        print(f"The computer chose {computer}.")

# DETERMINING THE WWINNER 
    if player == "Rock" and computer == "Paper":
        print("The computer won!")
    elif player == "Paper" and computer == "Rock":
        print("You won!")
    elif player =="Rock" and computer == "Scissors":
        print("You won!")
    elif player == "Scissors" and computer == "Rock":
        print("The computer won!")
    elif player == "Paper" and computer == "Scisssors":
        print("The computer won!")
    elif player == "Scissors" and player == "Paper":
        print("You won!")

    elif player == "Rock" and computer == "Rock":
        print("No winner!!!, \nPlay Again...")
    elif player == "Paper" and computer == "Paper":
        print("No winner!!!, \nPlay Again...")
    elif player  == "Scissors" and computer == "Scissors":
        print("No winner!!!, \nPlay Again...")

else:
    print("Please pick a number within range.")



# THE COURSES SOLUTION
user_choice = int(input("What do you choose?, Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

computer_choice = random.randint(0, 2) 
print(f"Computer chose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You won!")
elif computer_choice > user_choice:
    print("You lose!")
else:
    print("You typed an invalid number, you lose!")


# FINIRE