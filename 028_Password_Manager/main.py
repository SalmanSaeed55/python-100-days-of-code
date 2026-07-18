from pathlib import Path
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Salman's Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
logo_path = Path(__file__).resolve().parent / "logo.png"
logo = PhotoImage(file=str(logo_path))
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="w")
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email Address:")
email_label.grid(row=2, column=0, sticky="w")
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, sticky="w")

add_password = Button(text="Add Password", width=50)
add_password.grid(row=4, column=0, columnspan=3)


window.mainloop()