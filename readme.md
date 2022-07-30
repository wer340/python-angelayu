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
# calc
```python
number=12.23334343434
number=round(number,3)
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
---
# class inheritance modify class and give more capability
```python
class Animal:
    def __init__(self):
        self.num_eye=2
        self.num_feet=4
    def breathe(self):
        print("inhale and exhale ")
class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.num_feet=0
    def breathe(self):
        super().breathe()
        return "🌿🌿🌿🌿change origin method🌿🌿🌿🌿"
nemo=Fish()
print(f"num_feet = {nemo.num_feet} and method={nemo.breathe()}")
```
# slicing

```python
actress=['Mila Kunis', 'Jennifer Lawrence', 'Olivia Wilde', 'Nina Dobrev',
         'Evan Rachel Wood', 'Victoria Justice', 'Megan Fox', 'Blake Lively',
         'Amber Heard', 'Camilla Belle', 'Dianna Agron', 'Emma Watson']

print(len(actress))  #expect  12
print(actress[::3])  #expect  ['Mila Kunis', 'Nina Dobrev', 'Megan Fox', 'Camilla Belle']
print(actress[::-3])  #expect ['Emma Watson', 'Amber Heard', 'Victoria Justice', 'Olivia Wilde']
print(actress[6:])  #expect ['Megan Fox', 'Blake Lively', 'Amber Heard', 'Camilla Belle', 'Dianna Agron', 'Emma Watson']
```
---

# list and dict Comprehension   ☕☕✅💎
```python
names = ['Scarlett Johansson', 'Jennifer Lawrence', 'Emma Watson']           
new_list=[name.replace(" ","_") for name in names if len(name)<15]     
dict_names = {name: randint(1, 10) for name in names}  #sitution1️⃣list to dict 
dict_best_students={name:score for (name,score) in dict_names.items() if score>3 } #sitution2️⃣dict to new dict
# convert tuple for dict   in pandas moduls  data.iterrows(): 
```

---
# unlimited args **kwargs  keyword
```python
def calculator(n,**kwargs): ##kwargs type = dict
   n+=num.get("add")
   n*=num["mutiply"]
   return n
print(calculator(3,add=8,mutiply=2)) 
# *args  term of tuple 
```
## Python [Tutor](https://pythontutor.com/): Visualize code in Python, JavaScript, C, C++, and Java
##  [TRIVIA](https://opentdb.com/) Free to use, user-contributed trivia question database.
### fork it ❤   
