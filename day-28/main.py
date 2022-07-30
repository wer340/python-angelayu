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

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    countdown(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    # for each item create by canv define a name till change wiyh itemconfig
    canv.itemconfig(timer_text, text=count)
    if count > 0:
        tk.after(1000, countdown, count - 1)


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

start_b = Button(text="start", bg="white", highlightthickness=0,command=start_countdown)
start_b.grid(row=3, column=1)

reset_b = Button(text="reset", bg="white", highlightthickness=0)
reset_b.grid(row=3, column=3)

tick_l = Label(text="✔")
tick_l.grid(row=4, column=2)

tk.mainloop()
