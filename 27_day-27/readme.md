# [tkinter](https://www.tcl.tk/man/tcl/TkCmd/pack.html)  and  deafult value *args **kwargs(keyword)
Gaphical User Interfaace gui goiiiiiiiii 
+ history:lisa of apple  win 95 of  microsoft    both  stolen xerox parc   some people hire and work on gui
![gui](https://raw.githubusercontent.com/wer340/python-angelayu/main/27_day-27/images/gui.png)
# deafult value 
if parameter not set  deaafult value select 
```python
def banner(fname="scarlett",lname="  johansson"):
    print(fname+lname)
banner(lname="  emilia")
```
# unlimited arg without spicefy position 
 ✅tuple    this star a sign  for interpreter that get args  and put in tuple collection
```python
def add_sum(*numbers):  #deafult name *args
    print(type(numbers))  #tuple ~constant list
    print(numbers[14])
    return sum(numbers)
print(add_sum(3, 4, 6, 7, 8, 9, 4, 2, 1, 1, 4, 5, 6, 7, 88, 8, 8, 8, 8, 8))          
 ```
 # unlimited arg with spicefy position 
  ✅dict    this double star a sign  for interpreter that get args  and put in dictionary collection
  `n+=num.get("add")`  when use get method  if there isnt `add` arg python dont throw error   and reponse `undifiend`  but this way  `n*=num["mutiply"]` python throw error  
 ```python
 def calculator(n,**num): ##deafult name *kwargs  keyword args
    n+=num.get("add")
    n*=num["mutiply"]
    return n
print(calculator(3,add=8,mutiply=2))
```
----
# tkinter
![catalog](https://raw.githubusercontent.com/wer340/python-angelayu/main/27_day-27/images/tkinter_catlog.png)

---
pre install  tkinter
`windows=tkinter.Tk()`  not happen❌
it will go straight away to exit code zero and 
the reason for this is because we need a way of keeping the windows on the screen
what tkinter has done here is its gone ahead created athe window  sees that theres no more instructions
and then it basically ended the program now we want instead is to sort of have while loop that basically
just keep on runing so something like a while true and inside this while loop
it holds on to this window and keeps on linsting to see if there anything else that the user is going to
interact with that windows so that it can respond when that hapen 
so this loop in tkinter  all you have to do is get your window to simply ✅call `mainloop()`
mainloop bottom of project
### we use  `from tkinter import * `  

---
# pack place grid
```python
tk=Tk()
from tkinter import *
my_label=Label(tex="simple")
my_label.pack(side="left")
tk.mainloop()
```
widget next to each other in a vaguely logical format and by deafult pack will always start from the top and then pack every 
other widget just below the previous one   as i mention you can change this by adding a side parameter and you can change it 
the problem with pack is that its actually quite difficult to specify a precise position 
✅✅thats why there not just a single layout manager but there lots of others 
which is called ✔placed  💎place  is all about precise positioning  `my_label.place(x=,y=)`
another method   grid    `my_label.grid(column=,row=)`
only one method of 3 method use in project
```python
tk=Tk()
from tkinter import *
my_label=Label(tex="simple")
my_label.grid(column=3,row=2)
tk.mainloop()
```
