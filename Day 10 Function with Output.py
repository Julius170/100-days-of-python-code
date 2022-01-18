# FUNCTIONS WITH OUTPUT

def format_name(f_name, l_name):
    """Takes a first name and formats it to return 
    the little case version of the name. """
    if f_name == "" or l_name == "":
        return "You didn't provide a valid input."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"Result: {formatted_f_name} {formatted_l_name}"
    print("This got printed")


formatted_string = format_name(input("What is your first name: "), input("What is your last name: "))
print(formatted_string)


# COURSE'S SOLUTION
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def day_in_month(year, month):
    if month > 12 or month < 1:
        return "invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == True and month == 2:
        return 29
    return month_days[month - 1]


year = int((input("Enter a year: ")))
month = int(input("Enter a month: "))

days = day_in_month(year, month)
print(days)

# DOCSTRINGS: ARE WAYS TO CREATE DOCUMENTATIONS FOR OUR CODES
# EXAMPLES: lines 5 & 6
# USING THE (""" """) AS A MULTILINE COMMENT

"""    
THIS MEANS THAT (""" """ ) CAN ALSO BE USED 
TO WRITE A MULTILINE COMMENT  
"""


# CALCULATOR EXERCISE
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():  # RECURSION
    num1 = float(input("What's the first number?: "))
    for keys in operations:
        print(keys)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculator :") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()  # CALLING THE RECURSION


# print("This is a string")

calculator()

# FINITE
