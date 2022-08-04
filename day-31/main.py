from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
tk = Tk()
tk.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
tk.title("Capstone Flash Card ")
# TODO 2 csv to dict
with open("./data/french_words.csv") as file:
    dataframe = pd.read_csv(file)
    data=dataframe.to_dict(orient="records")

# TODO 3 generate word
def random_word():
    word=random.choice(data)
    canvas_t.itemconfig(card_title,text="French")
    canvas_t.itemconfig(card_word,text=word["French"])

# TODO 1 make UI
canvas_t = Canvas(width=800, height=526)
bg_image = PhotoImage(file="./images/card_front.png")
canvas_t.create_image(400, 263, image=bg_image)
card_title=canvas_t.create_text(400, 150, text="",
                           font=("Ariel", 40, "italic"))
card_word=canvas_t.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas_t.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_t.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_b = Button(image=wrong_img, highlightthickness=0,command=random_word)
wrong_b.grid(row=1, column=0)

correct_img = PhotoImage(file="./images/right.png")
correct_b = Button(image=correct_img, highlightthickness=0,command=random_word)
correct_b.grid(row=1, column=1)

random_word()
tk.mainloop()
