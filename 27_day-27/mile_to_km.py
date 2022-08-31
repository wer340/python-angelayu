from tkinter import *
import math
windows = Tk()
windows.minsize(width=250, height=250)
windows.title("mile to km calculator")

miles_l = Label(text="Miles ", font=("arial", 14))
miles_l.grid(column=3, row=1,padx=20,pady=10)

miles_i = Entry(width=20)
miles_i.grid(column=2, row=1,padx=10,pady=40)

is_equal_l = Label(text="is equal to  ", font=("arial", 14))
is_equal_l.grid(column=1, row=2,padx=10,pady=10)

km_l = Label(text="0", font=("arial", 14))
km_l.grid(column=2, row=2,padx=20,pady=10)

km_sticky_l = Label(text="Km", font=("arial", 14))
km_sticky_l.grid(column=3, row=2,padx=10,pady=10)


def calc():
    km = int(miles_i.get())
    km *= 1.6
    km=round(km,4)
    km_l["text"] = km


click_b = Button(text="Calculate lets go!", command=calc)
click_b.grid(column=2,row=3,padx=10,pady=10)
windows.mainloop()
