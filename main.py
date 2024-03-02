import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    passsword_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + passsword_numbers

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)

    password_entry.insert(END, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "Email": email,
        "Password": password
    }}

    # messagebox.showinfo(title="Title", message="Successfully added")
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as f:
                # saving updated data
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- search --------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo("Error", "No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lock = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.grid(column=1, row=0)
canvas.create_image(100, 100, image=lock)

website = Label(text="Website:")
website.grid(column=0, row=1)

website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()

search = Button(text="search", width=14, command=find_password)
search.grid(column=2, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_entry = Entry(width=50, )
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, "pavelsmida16@seznam.cz")

password = Label(text="Password:")
password.grid(column=0, row=3)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

password_generate = Button(text="Generate Password", width=14, command=generator)
password_generate.grid(column=2, row=3)

add = Button(text="Add", width=43, command=save)
add.grid(column=1, row=4, columnspan=2)



window.mainloop()