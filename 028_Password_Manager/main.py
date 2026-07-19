from pathlib import Path
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    messagebox.showinfo("Password Saved", f"Your Login information for {website_entry.get()} has been saved "
                                          f"successfully")

    with open("password.txt", "a") as file:
        file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Salman's Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_path = Path(__file__).resolve().parent / "logo.png"
logo = PhotoImage(file=str(logo_path))
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="w")
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email Address:")
email_label.grid(row=2, column=0, sticky="w")
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "salmansaeed1359@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, sticky="e")

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2, sticky="w")

add_password = Button(text="Add Password", width=50, command=save)
add_password.grid(row=4, column=0, columnspan=3)


window.mainloop()