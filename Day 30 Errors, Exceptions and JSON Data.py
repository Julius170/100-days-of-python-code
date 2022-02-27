# ERRORS EXCEPTIONS AND JSON DATA


# HANDLING ERRORS AND EXCEPTIONS 

# try:
# except:
# else:
# finally:

# # AN EXAMPLE
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"a_key": "a_value"}
#     print(a_dictionary["sdjvbniusbv"])
# except FileNotFoundError:
#     file = open("a_file.txt", "a")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("file was close.")
#     # RAISING EXCEPTIONS
#     raise TypeError("This is an error that i made up.")


# # EXERCISE 1

# fruits = ["Apple", "Pear", "Orange"]

# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:    
#         fruit = fruits[index]
#     except IndexError :
#         print("The number of list you've specified is out of range")
#         print("fruit pie")
#     else:
#         print(fruit + " pie")


# make_pie(4)
# SOLVED

# EXERCISE 2

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass

# print(total_likes)

# SOLVED


# MODIFYING THE NANO PHONETICS

# import pandas

# data = pandas.read_csv("NATO_phonetic_alphabets.csv")

# dictionary = (data.to_dict())
# new_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# def generate_phonetics():
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = (new_dict[letters] for letters in word)
#     except KeyError:
#         print("Sorry only letters in the alphabets please")
#     else:
#         print(output_list)

# generate_phonetics()


# MODIFYING THE PASSWORD GENERATOR APP IN DAY 29


from tkinter import *
from tkinter.messagebox import showinfo
import random
import pyperclip
import json

window = Tk()
from tkinter import messagebox

window.title("Password Manager")
window.config(padx=50, pady=50)


# GENERATING THE PASSWORD

def find_password():
    website = web_input.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email{email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)

    pyperclip.copy(password)


# SAVING THE PASSWORD
def saved_data():
    website = web_input.get()
    email = mail_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }
    if len(web_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="WARNING!", message="Please fill all the required information")
    else:
        try:
            with open("data.json", "r") as file:
                # json.dump(new_data, file, indent=4)      # TO MAKE A JSON FILE 
                data = json.load(file)  # TO READ JSON FILES WITH A NEW DATA
                # json.update(new_data)  # TO UPDATE THE JSON FILE
        except FileNotFoundError:
            with open("data.json", "a") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "a") as file:
                json.dump(new_data, file, indent=4)  # SAVING THE UPDATED FILE
                # file.write(f"{web_input.get()}  |  {mail_input.get()}  |  {password_input.get()}\n")
                # file.close()
        finally:
            web_input.delete(0, END)
            password_input.delete(0, END)


# PASSWORD GENERATION


# UI SETUP


canvas = Canvas(width=200, height=200)
# mypass = PhotoImage(file="hisrt's_image.jpg")
# canvas.create_image(100, 100, image=mypass)
canvas.grid(column=1, row=0)

# LABELS
web = Label(text="Website:")
web.grid(column=0, row=1)

mail = Label(text="Email/Username:")
mail.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

# ENTRIES
web_input = Entry(width=21)
web_input.grid(column=1, row=1)
web_input.focus()

mail_input = Entry(width=35)
mail_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=25)
password_input.grid(column=1, row=3, )

# BUTTON
gen_password = Button(text='Generate Password', command=generate_password)
gen_password.grid(column=3, row=3)

add_button = Button(text="Add", width=36, command=saved_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()

# FINITE
