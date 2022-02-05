# BUILDING A PASSWORD MANAGER


from tkinter import *
from tkinter.messagebox import showinfo
import random
import pyperclip

window = Tk()
from tkinter import messagebox

window.title("Password Manager")
window.config(padx=50, pady=50)


# GENERATING THE PASSWORD


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
    if len(web_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="WARNING!", message="Please fill all the required information")
    else:
        is_ok = messagebox.askokcancel(title=web_input.get(),
                                       message=f"These are the details entered: \n{mail_input.get()}"
                                               f"\n {password_input.get()}\n Is it Okay to Save")

        if is_ok:
            with open("day 29 saved_data.txt", "a") as file:
                file.write(f"{web_input.get()}  |  {mail_input.get()}  |  {password_input.get()}\n")
                # file.close()
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
web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
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

window.mainloop()



# FINITE