
# CONDITIONAL STATEMENTS
# LOGICAL OPERATORS
# CODE BLOOCKS AND SCOPE


# EXERCISE=> ODD OR EVEN

number = int(input("What number would you like to determine? "))
if (number % 2) == 0:
    print("The number you entered is an even number! \n")
else:
    print("The number you entered is an odd number! \n")


# EXERCISE=> A MODIFIED BMI CALCULATOR
weigth = int(input("Enter your weigth in kg: "))
heigth = float(input("Enter your heigth in meter: "))

bmi = weigth/(heigth ** 2)
bmi_result = int(bmi)

print (f"\nYour BMI is {round(bmi_result, 2)} therefore:\n")
if bmi_result < 18.5:
    print("Oh wow! You're seem to be UNDERWEITGH,\n That's not really good!\n ")
elif bmi_result < 25:
    print("Congratulation!, You're within the NORMAL weigth range,\n That's Awesome!\n")
elif bmi_result < 30:
    print("Hey!, Your a little OVERWEIGTH,\n You should be careful onward!\n")
elif bmi_result < 35:
    print("Oh Boy!, You're OBESE,\n You've got a lot of work to do Pal!\n")
else:
    print("Oh My!, Your are CLINICALLY OBESE,\n That's not good!\n")


#EXERCISE=> IS LEAP YEAR EXERCISE
# WRITE A PROGRAM THAT WORKS OUT IF THE GIVEN YEAR IS A LEAO YEAR.
# A NORMAL YEAR HAS 365 DAYS, LEAP YEARS HAVE 366, WITH AN EXTRA DAY IN FEBURARY.

# ON EVERY YEAR THAT IS EVENLY DIVISIBLE BY 4,
# EXCEPT EVERY YEAR THAT IS EVENLY DIVISIBLE BY 100,
# UNLESS THE YEAR IS ALSO EVENLY DIVISIBLE BY 400.


# MY SOLUTION
year = int(input("What year would you like to determine: "))
year4 = year % 4
year100 = year % 100
year400 = year % 400

if year4 == 0 and year400 == 0 :
    print (f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")

#                              OR
# COURSE'S SOLUTION
# if year % 4  == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year.")
#         else:
#             print("Not Leap Year.")
#     else:
#         print("Leap Year.")
# else:
#     print(f"Not Leap Year.")




# EXERCISE=> PAYING FOR A RIDE IN THE PARK

heigth = int(input("How tall are you (cm)? "))
if heigth >= 120:
    age = int(input("How old are you? \n"))

    if age < 12:
        bill = 5
        ticket = int(input("A ticket will be $5, how many would you like? \n"))
    elif age < 18:
        bill = 7
        ticket = int(input("A ticket will cost $7,how many would you like? \n"))
    elif age < 45:
        bill = 12
        ticket = int(input("A ticket will be $12, how many would you like? \n"))
    elif age <= 55:
        bill = 0
        ticket = 0
        print("Everything is Okay, You can have a free ride on us! ")

    picture = input("would you like to take photos? Y or N? ")
    if picture == "Y":
        print(f"Your bill will be: ${bill * ticket + 3 }\n")
    elif picture == "N":
        print(f"Your bill will be: ${bill * ticket}\n")
    else:
        print("Incorrect Input!\n")

else:
    print("Sorry Pal!, you're not tall enough, ticket cannot be sold!.\n")





# EXERCISE 3.4 => PIZZA ORDER EXERCISE

print("Welcome to Python Pizza Dilervery!\n")

size = input("What size  do you want? S, M, L \n")

pepperoni = input("Would you like the Pepperoni topping? Y or N \n")

cheese = input("Would you like Extra Cheese? Y or N \n")


bill = 0
if size == "S" :
    bill += 15
elif size == "M" :
    bill += 20
elif size == "L":          # NB=> "ELSE" IS NOT NECCESARY WITH "ELIF"
    bill += 25
else:
    print("Incorrect Input!")

if pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill+=3

if cheese == "Y":
    bill +=1

print(f"Your final bill is ${bill}")


# LOVE CALCULATOR EXERCISE=>
print("Welcome to the Love Calculator!")

name1 = (input("What is your name? \n"))
name2 = (input("What is their name? \n"))

Lovers_Name = (name1 + name2).lower()

t = Lovers_Name.count("t")
r = Lovers_Name.count("r")
u = Lovers_Name.count("u")
e = Lovers_Name.count("e")
true = (t+r+u+e)

l = Lovers_Name.count("l")
o = Lovers_Name.count("o")
v = Lovers_Name.count("v")
e = Lovers_Name.count("e")
love = (l+o+v+e)

total = int(str(true) + str(love))

# total_int = (f"{total}%")

if total < 10 or total > 90:
    print(f"Your Score is {total}%, you go together like coke and mentos.")
elif total >= 40 or total < 50:
    print(f"Your score is {total}%, you are alright together.")
else:
    print(f"Your score is {total}%")


# FINAL EXERCISE=> DAY 3 FINAL PROJECT: TREASURE HAUNTING
# MY SOLUTION
print("Welcome to Treasure Haint Island, Your mission is to find the treasure.")

turn = input("Would you like to go left or right? ")
if turn  == "right":
    print("Great Job! \nkeep moving...\n")
elif turn == "left":
    print("Oops! You're stuck in a trap, \nGame Over!")
else:
    print("Oops!")


choice = input("Would you like to wait or go swim? ")
if choice == "wait":
    print("Congrats! You're still Alive...")
elif choice == "swim":
    print("Oh my! You didn't make it. \n Try Again! ")
else:
    print("Huh!!!...")


door = input("What colour of door would you like to open? ")
if door == "red":
    print("Oh you were soo close!  Game Over... \n Try Again")
elif door == "blue":
    print("Oh you were soo close!  Game Over... \n Try Again")
elif door == "yellow":
    print("Congratulation! YOU WIN!!!...")
else:
    print("No Answer for that Pal!!!...")


# COURSE'S SOLUTION:

print ("Welcome to Treasure Island")
print("Your mission is to find the treasure.\n")
choice1 = input("you're at a crossroad, where do want to go to? Type 'left' or 'right' \n").lower()

if choice1 == "left":
    choice2 = input("You've come  to a lake, where do you wnt to go, Type 'wait' to wait for a boat. Type 'swim' ro swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island unharmed. There is a house with 3 doors, one yellow, and one blue. \nWhat coloured door would you like to open? \n")
        if choice3 == "red":
            print("It's a room full of fire. Game Over\n")
        elif choice3 == "yellow":
            print("You found  the treasure. Your Win!\n")
        elif choice3 == "blue":
                print("You've entered aa room of beasts. Game Over.\n")
        else:
            print("You chose a dor that doesn't exist. Game Over.\n")
    else:
        print("You got attacked by an angry trout. Game Over\n")
else:
    print("You fell into a hole Game Over.\n")

# FINIRE