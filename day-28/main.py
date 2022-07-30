from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = .15
LONG_BREAK_MIN = 20
reps = 0  # repetion


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    # first reps declare next line  reps work
    global reps
    reps+=1
    work_min_sec = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    if reps%8==0:
        countdown(long_break_min)
        timer_l.config(fg=RED)
    elif reps%2==0:
        countdown(short_break_min)
        timer_l.config(fg=PINK)
    else:
        countdown(work_min_sec)
        timer_l.config(fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    # for each item create by canv define a name till change wiyh itemconfig
    time_min = math.floor(count / 60)
    time_sec = math.floor(count % 60)
    if time_sec < 10:
        time_sec = f"0{time_sec}"
    canv.itemconfig(timer_text, text=f"{time_min}:{time_sec}")
    if count > 0:
        tk.after(1000, countdown, count - 1)
    else:
        start_countdown()
# ---------------------------- UI SETUP ------------------------------- #


tk = Tk()
tk.title("Pomodoro Technic")
tk.config(padx=100, pady=50, bg=YELLOW)

timer_l = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 35, "bold"),
                fg=GREEN)
timer_l.grid(row=1, column=2)
canv = Canvas(width=200, height=224, bg=YELLOW)
image = PhotoImage(file="./tomato.png")
canv.create_image(102, 110, image=image)
timer_text = canv.create_text(100, 113, text="00:00",
                              font=(FONT_NAME, 25, "bold"),
                              fill="white")
canv.grid(row=2, column=2)

start_b = Button(text="start", bg="white", highlightthickness=0,
                 command=start_countdown)
start_b.grid(row=3, column=1)

reset_b = Button(text="reset", bg="white", highlightthickness=0)
reset_b.grid(row=3, column=3)

tick_l = Label(text="✔")
tick_l.grid(row=4, column=2)

tk.mainloop()
