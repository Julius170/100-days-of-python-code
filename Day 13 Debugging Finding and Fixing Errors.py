# DEBUGGING
# GRACE HOPPER == PROPOUNDED THE IDEA OF BUGS IN CODES

# STEPS TO APPROACH WHEN FINDING AND FIXING BUGS 

# 1. DESCRIBE THE PROBLEM

# def my_function():
#     for i in range(1, 21):     # CHANGED 20 TO 21
#         if i == 20:
#             print("You get it")
# my_function()
        
# 2. REPRODUCING THE BUG

# from random import randint 
# dice_imgs = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"]
# dice_num = randint(0, 5)          # CHANGED 6 TO 5 
# print(dice_imgs[dice_num])
        

# 3. PLAY COMPUTER

# year = int(input("What's your year of birth? "))
# if year > 1980 and year <= 1994:
#     print("You're a Millenial.")
# elif year >= 1994:                  # ADDED THE '=' SIGN 
#     print("You are a Gen Z.")


# 4. FIX THE ERRORS
# age = int(input("How old are you? ")) # ADDED THE 'INT' FUNTION
# if age > 18:
#     print(f"You can drive at age {age}")


# # 5. PRINT IS YOUR FRIEND (USE THE PRINT FUNCTION MORE OFTEN)
# pages = 0 
# word_per_pages = 0
# pages = int(input("Number of pages: "))
# word_per_pages = int(input("Number of words per pages: "))    #REMOVED ONE '=' SIGN
# total_words = pages * word_per_pages
# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_pages}")
# print(total_words)


# # 6. USE A DEBUGGER
# def  mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)   # ADDED AN INDENT 
#     print(b_list)
    
    
# mutate([1, 2, 3, 5, 8, 13])       # REMOVED AN INDENT

# DEBUGGING FINAL TECHNIQUES

# 7. TAKE A BREAK (RATHER THAN STARING ON THE SCREEN)

# 8. ASK A FRIEND

# 9. RUN YOUR CODE OFTEN (NOT AFTER A WHOLE PILE OF CODE)

# 10. ASK STACKOVERFLOW



# # DEBUG ODD OR EVEN EXERCISE

# number = int(input("Which nymber do you want to check?"))

# if number % 2 == 0:  # ADDED ANOTHER '=' SIGN
#     print("This is en even number.")
# else:
#     print("This is an odd number.")
    

# # DEBUG LEAP YEAR EXERCISE

# year = int(input("Which year do you want to check?"))  # ADDED THE 'INT' FUNCTION  

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")
    



# # DEBUG FIZZ BUZZ EXERCISE

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:   #CHANGED THE 'or' TO 'and'
#         print("FizzBuzz")
#     elif number % 3 == 0:  # CHANGED THE 'if' to 'elif'
#             print("Fizz")
#     elif number % 5 == 0:  # CHANGED THE 'f' to 'elif'
#             print("Buzz")
#     else:
#         print(number)  # REMOVED THE '[]' LIST SQUARE BRACKET
    





