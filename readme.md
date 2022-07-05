# 100day python Angela Yu ✅🌿
---
### IDE [`I`ntelligent `D`evelopment `E`nviroment] useful shortcut keyBoard
|vscode|description|pycharm|description|
|------------|-----------|------------|-----------|
|Alt+Shift+Arrow key|copy line|Alt+shift▶then drag down|some cursor creaate for type same thing|
|Ctrl+] and Ctrl+[|adjust indent|Command+Alt+L and [Wrapping and Braces](https://stackoverflow.com/questions/57302273/how-to-split-one-very-long-line-in-pycharm-into-multiple-lines)|break long line|
|Alt+z|break long line|Alt+enter|reformat code|

---
### type of variable

```python
def my_function():
  return[name]
 
 print(type(my_function())
 ```

+ **list.append(elem)** -- adds a single element to the end of the list. Common error: does **not return** the new list, just modifies the original.
+ **list.insert(index, elem)** -- inserts the element at the **given index**, shifting elements to the right.
+ **list.extend(list2)** or **[]+=[]** adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
+ **list.index(elem)** -- searches for the **given element** from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
+ **list.remove(elem)** -- searches for the first instance of the **given element** and removes it (throws ValueError if not present)
+ **list.sort()** -- sorts the list in place (does **not return** it). (The sorted() function shown later is preferred.)
+ **list.reverse()** -- reverses the list in place (does **not return** it)
+ **list.pop(index)** -- removes and returns the element at the given index. **Returns** the rightmost element if index is omitted (roughly the opposite of append()).
# python list 
```python
fruits=[item1,item2]
list.append(x) #add item
fruits[-1]   #output=item2 if offset start last list
str_inp = "Hello,from,AskPython"
op = str_inp.split(",")
print(op)
```
# python  dictionary
```python
list_dictionary={
"Scarlett Johansson":"Avengers: Endgame",
"Sharon Stone":"Basic Instinct",
"Jennifer Connelly":"A Beautiful Mind",
"Brooke Shields":"The Blue Lagoon",
"Monica Bellucci":"Malena"
}
list_dictionary["Angelina Jolie"]="Maleficent" #add record
```
### oop
```python
from turtle import Turtle,Screen   #PascalCase   CodeCase 
#which is normally written with the first letter of each word capitalized which is known as ✔pascal case
timmy=Turtle()  
my_screen=Screen() 
print(timmy)   //expect  adress of loaction
my_screen.cancheight #object attribute  output value height 
my_screen.exitonclick() #method
timmy.forward(44)#method
```
## Python [Tutor](https://pythontutor.com/): Visualize code in Python, JavaScript, C, C++, and Java
### fork it ❤   
