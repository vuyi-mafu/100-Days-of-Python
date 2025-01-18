from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def generate_pass():
    password_input.delete(0, END)

    letter_list = [random.choice(letters) for letter in range(nr_letters)]
    symbol_list = [random.choice(symbols) for symbol in range(nr_symbols)]
    number_list = [random.choice(numbers) for number in range(nr_symbols)]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, f"{password}")

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_entry = website_input.get()
    username_entry = username_input.get()
    password_entry = password_input.get()

    if len(website_entry) == 0 or len(password_entry) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry,
                                       message=f"These are the details entered: \nEmail: {username_entry} "
                                               f"\nPassword: {password_entry} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_entry} | {username_entry} | {password_entry}\n")
            website_input.delete(0, END)
            # username_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# window.minsize(400, 400)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_logo)
canvas.grid(column=1, row=0)

#   Labels
website_label = Label()
website_label.config(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label()
username_label.config(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label()
password_label.config(text="Password:")
password_label.grid(column=0, row=3)

#   Input Boxes
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "vuyimafu@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#   Buttons
generate_password = Button()
generate_password.config(text="Generate Password", command=generate_pass)
generate_password.grid(column=2, row=3)

add_button = Button()
add_button.config(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
