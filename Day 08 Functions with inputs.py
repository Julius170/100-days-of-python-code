# FUNCTION WITH INPUTS 
# ARGUMENTS AND PARANETERS



def greet_with(name, location):
    print(f"Hello {name}")
    
    print(f"What is it like in {location}")
  
greet_with("Henry Cavil", "New York")
  
  
  
# AREA CALCULATION EXERCISE
wall_heigth = int(input("What is the heigth of the wall? "))  
wall_width = int(input("What is the Width of the wall? "))
coverage = 5
  
result = (wall_heigth * wall_width) / coverage

print(f"You need {round(result)} number of paints for the wall")
  
  
from math import ceil 
def calc(heigth, width, coverage):
    area = heigth *width
    result = area / coverage
    print(f"You need {ceil(result)} cann of paints for the wall")
  
  
calc(heigth = 2, width = 10, coverage = 5)


# CEASER'S CIPHER
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
while should_continue == True: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ")
    text = input("Type Your messagge:\n ").lower()
    shift = int(input("Type the shift number:\n "))

    result = input(f"Type 'yes' if you wanna go again otherwise type 'no'.\n")
    shift = shift % 25

# MY FINAL SOLUTION
    def ceaser (start_text, shift_amount, cipher_direction):
        end_text = ""
        for char in start_text:
            if char in alphabets:
                position = (alphabets.index(char))
                # HER SOLUTION
                # if cipher_direction == "decode":
                #     shift_amount *= -1
                # new_letters = position + shift_amount
                # end_text += alphabets[new_position]
                if cipher_direction == "encode":
                    new_position = position + shift_amount
                elif cipher_direction == "decode":
                    new_position = position - shift_amount
                new_letters = alphabets[new_position]
                end_text += new_letters
            else:
                end_text += char
            
        print(f"Your {cipher_direction}d text is {end_text}")
                
            
    ceaser(start_text = text, shift_amount = shift, cipher_direction = direction)

    if result == "no":
        should_continue = False
        print("Good Bye")



# FINIRE