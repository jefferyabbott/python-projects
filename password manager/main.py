from tkinter import *
from tkinter import messagebox
from password_generator import generate_random_password
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    generated_password = generate_random_password()
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# --------------------------- SEARCH PASSWORD ------------------------------ #
def search_passwords():
    search_term = website_entry.get()
    if search_term == '':
        messagebox.showinfo(title="Missing website", message="Please enter a website.")
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            message = f"Website: {search_term}\nUsername/Email: {data[search_term]['email']}\nPassword: {data[search_term]['password']}"
            messagebox.showinfo(title=f"{search_term} details", message=message)
    except FileNotFoundError:
        messagebox.showinfo(title="Missing data file", message="There is no data to search.")
    except KeyError as error_message:
        messagebox.showinfo(title="Website not found", message="This website was not found in the data file.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == '' or email == '' or password == '':
        messagebox.showinfo(title="Missing info!", message="Please enter all required information.")
        return

    confirmation = f"Details entered:\nEmail: {email}\nPassword: {password}\n\nOk to save?"
    is_ok = messagebox.askokcancel(title=website, message=confirmation)

    if not is_ok:
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search", width=13, command=search_passwords)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()