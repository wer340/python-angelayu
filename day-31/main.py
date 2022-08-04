from tkinter import *
import pandas as pd
import random
import time

global word, flip_timer
BACKGROUND_COLOR = "#B1DDC6"

# TODO 2 csv to dict
with open("./data/french_words.csv") as file:
    dataframe = pd.read_csv(file)
    data = dataframe.to_dict(orient="records")


# TODO 4  show back of card  that's english mean

def back_card():
    canvas_t.itemconfig(card_image, image=back_image)
    canvas_t.itemconfig(card_title, text="English")
    canvas_t.itemconfig(card_word, text=word["English"])


# TODO 3 generate word
def random_word():
    global word,flip_timer
    tk.after_cancel(flip_timer) # for each time run function separately counted timer
    word = random.choice(data)
    canvas_t.itemconfig(card_image,image=front_image)
    canvas_t.itemconfig(card_title, text="French")
    canvas_t.itemconfig(card_word, text=word["French"])
    flip_timer=tk.after(3000,back_card) #run timer every next otherwise  back_card run first time

# TODO 1 make UI
tk = Tk()
tk.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
tk.title("Capstone Flash Card ")
flip_timer = tk.after(3000, back_card)

canvas_t = Canvas(width=800, height=526)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card_image = canvas_t.create_image(400, 263, image=front_image)
card_title = canvas_t.create_text(400, 150, text="",
                                  font=("Ariel", 40, "italic"))
card_word = canvas_t.create_text(400, 263, text="",
                                 font=("Ariel", 60, "bold"))
canvas_t.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_t.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_b = Button(image=wrong_img, highlightthickness=0,
                 command=random_word)
wrong_b.grid(row=1, column=0)

correct_img = PhotoImage(file="./images/right.png")
correct_b = Button(image=correct_img, highlightthickness=0,
                   command=random_word)
correct_b.grid(row=1, column=1)

random_word()
tk.mainloop()
