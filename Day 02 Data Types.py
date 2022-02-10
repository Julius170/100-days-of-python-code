# DATA TYPES 

# STRINGS
print("Hello"[4])
print("123" + "456")

# INTERGERS
print(123 + 456)

# FLOATS 
3.142

# BOOLEAN
True
False

num_char = len(input("What's your name?"))
new_num_char = str(num_char)
print("Your name contains " + new_num_char + " characters")

a = float(123)
print(type(a))

print(70 + float("100.5"))

# EXERCISE
two_digit_number = input("Type a two digit number: ")
print(type(two_digit_number))

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)

print(result)


# MATHEMATICAL OPERATIONS ("+", "-", "*", "/", "**") 
# PEMDAS-LR=> PARENTHESIS(), EXPONENTS**, MULTIPLICATION*, DIVISION/, ADDITION+, SUBTRACTION-, LEFT TO RIGHT

# EXERCISE=> BMI CALCULATOR
# BMI = WEIGHT(KG)/HEIGTH**2(m**2)

weigth = int(input("Enter your weigtth in kg: "))
heigth = float(input("Enter your heigth in meter: "))

bmi = (weigth/heigth ** 2)
bmi_as_int = int(bmi)

print (f"Your BMI is {bmi_as_int}kg/m**2")

# ROUNDING NUMBERS
print(round(8/3, 3))



# EXERCISE
current_age = int(input("What is your current age: "))
days_left = (365*90) - (current_age*365) 
weeks_left = (52*90) - (current_age*52)
months_left = (12*90) - (current_age*12)

print(f"You have {days_left} days, {weeks_left} weeks and {months_left}months left.")

# EXERCISE=> TIP CALCULATOR

print("Welcome to the tip calculator.\n")
bill = float(input("what was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?")) 
people = int(input("How many people are to split the tip?"))

tip_to_pay =  (bill * (tip/100) + bill)/people 

print(f"Each person should pay: ${round(tip_to_pay, 2)} ")

# FINIRE
