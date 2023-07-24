import tkinter
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


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps == 1:
        countdown(work_sec)
        timer_label.config(text="working time")
        check_marks.config(text="_/")
    if reps == 2:
        countdown(short_break_sec)
        timer_label.config(text="short break")
    if reps == 3:
        countdown(work_sec)
        timer_label.config(text="working time")
        check_marks.config(text="_/_/")
    if reps == 4:
        countdown(short_break_sec)
        timer_label.config(text="short break")
    if reps == 5:
        countdown(work_sec)
        timer_label.config(text="working time")
        check_marks.config(text="_/_/_/")
    if reps == 6:
        countdown(short_break_sec)
        timer_label.config(text="short break")
    if reps == 7:
        countdown(work_sec)
        timer_label.config(text="working time")
        check_marks.config(text="_/_/_/_/")
    if reps == 8:
        countdown(long_break_sec)
        timer_label.config(text="long break")



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(100, countdown, count - 1)
    if count <= 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pamadoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.after(1000, )

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoe_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoe_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", fg="black", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", fg="black", command=reset)
reset_button.grid(column=2, row=2)

check_marks = tkinter.Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)

window.mainloop()
