import tkinter


windows=tkinter.Tk()
windows.minsize(width=600,height=400)
windows.title("first program")

tinker=tkinter.Label(text="I am a label ",font=("arial",30))
tinker.pack(side="bottom")#left right


windows.mainloop()