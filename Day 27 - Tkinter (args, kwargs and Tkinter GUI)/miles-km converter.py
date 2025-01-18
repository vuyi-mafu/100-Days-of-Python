from tkinter import *


def calculate_kilometres():
    miles = float(input_box.get())
    km = round((miles * 1.60934), 2)
    value_label.config(text=f"{km}")


window = Tk()
window.minsize(width=300, height=120)
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

#   First label
is_equal_to = Label()
is_equal_to.config(text="is equal to")
is_equal_to.grid(column=0, row=1)

#   Second Label
value_label = Label()
value_label.config(text="0")
value_label.grid(column=1, row=1)

#   Third Label
km_label = Label()
km_label.config(text="Km")
km_label.grid(column=2, row=1)

#   Fourth Label
miles_label = Label()
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)

#   Button
button = Button()
button.config(text="Calculate", command=calculate_kilometres)
button.grid(column=1, row=2)

input_box = Entry()
input_box.config(width=10)
input_box.insert(0, "0")
input_box.grid(column=1, row=0)


window.mainloop()
