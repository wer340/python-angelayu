from tkinter import *
import requests

tk=Tk()
tk.title("kanye west Quote ...")

def get_quote():
    response=requests.get("https://api.kanye.rest/")
    response.raise_for_status()
    data=response.json()
    quote=data["quote"]
    canvas.itemconfig(canvas_quote,text=quote)

canvas=Canvas(height=500,width=400)
bg=PhotoImage(file="bg.png")
canvas.create_image(250,200,image=bg)
canvas_quote=canvas.create_text(170,200,text="kanye west goes here",width=300,font=("Arial",15) )
canvas.grid(row=0,column=0)
bg_button=PhotoImage(file="bg_button.png")
button=Button(image=bg_button,highlightthickness=0,command=get_quote)
button.grid(row=1,column=0)









tk.mainloop()