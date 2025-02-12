from tkinter import *


def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#   Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

#   Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#   Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


window.mainloop()
