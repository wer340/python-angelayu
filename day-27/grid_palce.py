import tkinter

windows = tkinter.Tk()
windows.minsize(width=600, height=400)
windows.title("first program")
windows.config(padx=100,pady=200)
my_label = tkinter.Label(text="I am a label ", font=("arial", 30))
my_label.grid(column=1,row=4)  # side=left right
#my_label.place(x=0,y=100)


# Button Class
def click_btn():
    my_label["text"]=entry.get()
    print("click to me !")


button = tkinter.Button(text="click Me ", command=click_btn)
button.grid(column=3,row=4)

#Entry Class
entry=tkinter.Entry(width=20)
print(entry.get())
entry.grid(column=4,row=12)

windows.mainloop()
