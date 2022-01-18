# FOR LOOPS, RANGE AND CODE BLOCK

# FOR LOOPS
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:  # ONLY APPLY TO STATEMENTS INDENTED AFTERWARDS
    print(fruit)
    print(fruit + "Pie")

print('fruits')

# EXERCISE : AVERAGE SIZE
heights = input("input a list of student heights? ").split()
for n in range(0, len(heights)):  # TURNING THE INPUTS INTO AN INT
    heights[n] = int(heights[n])
print(heights)

height_sum = 0
for nums in heights:
    height_sum += nums
# print(height_sum)

num_of_heights = 0
for figs in heights:
    num_of_heights += 1
# print (num_of_heights)

average_height = round((height_sum / num_of_heights), 3)

print(f"The average height of the students is {average_height}")

# EXERCISE: HIGHEST SCORE

scores = input("Input the list of student scores: ").split()
for p in range(0, len(scores)):
    scores[p] = int(scores[p])
print(scores)

highest = 0
for score in scores:
    if score > highest:
        highest = score

print(f"The highest score in thr class is: {highest}")

# FOR LOOP WUTH RANGE

for number in range(1, 11, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

# EXERCISE: ADDING EVEN

number_sum = 0
for digits in range(2, 101, 2):
    number_sum += digits
print(number_sum)

# OR

# total2 = 0
# for number in range(2, 101, 2):
#     if number % 2 == 0:
#         total2 += number
# print(total2)


# constant = 0
for ints in range(1, 101):
    if ints % 15 == 0:  # OR (ints % 3 == 0 and ints % 5 == 0)
        print("FizzBuzz")
    elif ints % 3 == 0:
        print("Fizz")
    elif ints % 5 == 0:
        print("Buzz")
    else:
        print(ints)

# EXERCISE: PY PASSWORD GENERATOR
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

nr_letters = int(input("How many letters would you like in your password: \n"))
nr_numbers = int(input("How many numbers would you like in your password: \n"))
nr_symbols = int(input("How many symbols would you like in your password: \n"))

# # EASY LEVEL
# password = ""
# for lets in range(1, nr_letters + 1):
#     password += random.choice(letters)

# SELECTING THE RANDOM CHARACTERS FROM THE VARIABLES ABOVE AND ADDING TO THE ARRAY


# for nums in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# for sums in range(1, nr_symbols +1):
#     password += random.choice(symbols)

# print(password)


# HARD LEVEL
password_list = []
for lets in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# SELECTING THTE RANDOM CHARACTERS FROM THE VARIABLES ABOVE AND ADDING TO THE ARRAY

for nums in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

for sums in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

# print(password_list)
random.shuffle(password_list)  # RANDOMIZING THE PASSWORD
# print(password_list)

password = ""  # TURNING THE ARRAY TO A STRING
for chars in password_list:
    password += chars

print(f"Your password is {password}")

# FINITE
