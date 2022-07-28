# [tkinter](https://www.tcl.tk/man/tcl/TkCmd/pack.html)  and  deafult value *args **kwargs(keyword)
Gaphical User Interfaace gui goiiiiiiiii 
+ history:lisa of apple  win 95 of  microsoft    both  stolen xerox parc   some people hire and work on gui

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
 ```python
 def calculator(n,**num): ##deafult name *kwargs  keyword args
    n+=num.get("add")
    n*=num["mutiply"]
    return n
print(calculator(3,add=8,mutiply=2))
```
----
# tkinter
