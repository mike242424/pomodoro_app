from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    check_label["text"] = ''
    canvas.itemconfig(timer_text, text='15:00')
    

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="PINK", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f'0{str(seconds)}'
    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        if reps % 2 == 0:
            check_label.config(text="✔", fg=GREEN)
        elif reps % 4 == 0:
            check_label.config(text="✔✔", fg=GREEN)
        elif reps % 6 == 0:
            check_label.config(text="✔✔✔", fg=GREEN)
        elif reps % 8 == 0:
            check_label.config(text="✔✔✔✔", fg=GREEN)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=70, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=bg_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', command=start_timer, fg=GREEN, font=(FONT_NAME, 18, 'bold'), highlightthickness=0)
start_button.grid(column=0, row=2)

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35))
check_label.grid(column=1, row=3)

reset_button = Button(text='Reset', command=reset_timer, fg=GREEN, font=(FONT_NAME, 18, 'bold'), highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()

