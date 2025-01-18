from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    window.after_cancel(timer)
    timer_label.config(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
    tick_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    #   If it's the 1st/3rd/5th/7th rep:
    if reps % 2 == 1 and reps != 8:
        timer_label.config(text="Work", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
        countdown(work_sec)

    #   If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0 and reps != 8:
        timer_label.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=PINK, bg=YELLOW)
        countdown(short_break_sec)

    #   If it's the 8th rep:
    elif reps % 8 == 0:
        timer_label.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=RED, bg=YELLOW)
        countdown(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        tick = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            tick += "✔"
        tick_label.config(text=tick)


# ---------------------------- UI SETUP ------------------------------- #\
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#   Setup Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#   Setup Start and Reset Buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_time)
reset_button.grid(column=2, row=2)

#   Setup Timer Label
timer_label = Label()
timer_label.config(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

#   Tick Label
tick_label = Label()
tick_label.config(fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=4)

window.mainloop()
