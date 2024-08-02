from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #


def reset_time():
    check_label["text"] = ''
    canvas.itemconfig(text_id, text='00:00')


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=70, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=bg_img)
text_id = canvas.create_text(100, 130, text='15:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', command=reset_time, fg=GREEN, font=(FONT_NAME, 18, 'bold'), highlightthickness=0)
start_button.grid(column=0, row=2)

check_label = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35))
check_label.grid(column=1, row=3)

reset_button = Button(text='Reset', command=reset_time,fg=GREEN, font=(FONT_NAME, 18, 'bold'), highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()

