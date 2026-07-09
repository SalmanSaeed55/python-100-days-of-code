from tkinter import *


def miles_to_km():
    miles = miles_inp.get()
    km = float(miles) * 1.609
    km_results.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(200, 200)
window.config(padx=50, pady=70)
window.resizable(False, False)

miles_inp = Entry(window, width=7)
miles_inp.grid(row=0, column=1)

miles_label = Label(window, text="Miles")
miles_label.grid(row=0, column=2)

is_equal = Label(window, text="is equal to")
is_equal.grid(row=1, column=0)

km_results = Label(window, text="")
km_results.grid(row=1, column=1)

km_label = Label(window, text="Kilometers")
km_label.grid(row=1, column=2)

calc_btn = Button(window, text="Calculate", command=miles_to_km)
calc_btn.grid(row=2, column=1)

window.mainloop()