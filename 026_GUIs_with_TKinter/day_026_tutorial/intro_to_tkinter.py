import tkinter

def button_clicked():
    hello = tkinter.Label(text="Hello")
    hello.pack()

window = tkinter.Tk()
window.title("First GUI Program")
window.geometry("400x300")

my_label = tkinter.Label(window, text="I am a label", font=("Arial", 25, "bold"))
my_label.pack(side="left")

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack(side="right")

inp = tkinter.Entry(width=20)
inp.pack(side="left")

window.mainloop()