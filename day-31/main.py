from  tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

tk=Tk()

tk.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
tk.title("Capstone Flash Card ")


canvas=Canvas(width=800,height=526)
bg_image=PhotoImage(file="./images/card_front.png")
canvas.create_image(400,263,image=bg_image)
canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.config(highlightthickness=0,bg=BACKGROUND_COLOR)
canvas.grid(row=0,column=0,columnspan=2)
wrong_img=PhotoImage(file="./images/wrong.png")
wrong_b=Button(image=wrong_img,highlightthickness=0)
wrong_b.grid(row=1,column=0)
correct_img=PhotoImage(file="./images/right.png")
correct_b=Button(image=correct_img,highlightthickness=0)
correct_b.grid(row=1,column=1)
tk.mainloop()