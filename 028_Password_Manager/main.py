from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Salman's Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
canvas.pack()

window.mainloop()