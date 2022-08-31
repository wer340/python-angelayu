import tkinter

windows = tkinter.Tk()
windows.minsize(width=600, height=400)
windows.title("first program")

my_label = tkinter.Label(text="I am a label ", font=("arial", 30))
my_label.pack()  # side=left right
my_label["text"] = "Flower natherland"  # overwrite
my_label.config(text="Germany")  # overwrite


# Button Class
def click_btn():
    my_label["text"]=entry.get()
    print("click to me !")


button = tkinter.Button(text="click Me ", command=click_btn)
button.pack()

#Entry Class
entry=tkinter.Entry(width=20)
print(entry.get())
entry.pack()

windows.mainloop()
