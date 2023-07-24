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

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    countdown(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count -1)

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

reset_button = tkinter.Button(text="Reset", fg="black")
reset_button.grid(column=2, row=2)

check_marks = tkinter.Label(text="_/", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)



window.mainloop()
