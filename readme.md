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
list
dict 
string 
int
float
tuple
```python
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}
print(type(mytuple))
 ```


---
# [mutable  vs immutaable](https://www.pythontutorial.net/advanced-python/python-mutable-and-immutable)
+ An object whose internal state cannot be changed is called **immutable** for example a number, a string, and a tuple.
+ An object whose internal state can be changed is called **mutable** for example a list, a set, and a dictionary
```python
#mutable
ratings = [1, 2, 3]
print(hex(id(ratings)))# 0x1840f97a340
ratings.append(4)
print(ratings)  # [1, 2, 3, 4]
print(hex(id(ratings)))# 0x1840f97a340
#immutble
counter = 100
print(hex(id(100)))#0x7ffb62d32300
counter = 200
print(hex(id(counter))) #0x7ffb62d32f80
```

# python list 
+ **list.append(elem)** -- adds a single element to the end of the list. Common error: does **not return** the new list, just modifies the original.
+ **list.insert(index, elem)** -- inserts the element at the **given index**, shifting elements to the right.
+ **list.extend(list2)** or **[]+=[]** adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
+ **list.index(elem)** -- searches for the **given element** from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
+ **list.remove(elem)** -- searches for the first instance of the **given element** and removes it (throws ValueError if not present)
+ **list.sort()** -- sorts the list in place (does **not return** it). (The sorted() function shown later is preferred.)
+ **list.reverse()** -- reverses the list in place (does **not return** it)
+ **list.pop(index)** -- removes and returns the element at the given index. **Returns** the rightmost element if index is omitted (roughly the opposite of append()).

```python
fruits=[item1,item2]
fruits_string=''.join(fruits)#whithout number if have number first  map(str,list)
list.append(x) #add item
fruits[-1]   #output=item2 if offset start last list
str_inp = "Hello,from,AskPython"
op = str_inp.split(",")
print(op)
# using the enumerate() function to get index 
for i, d in enumerate(fruits):
    print (i, d)  #expect  0 item1    \n  1 item2
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
---
# dynamic typing
change a variable data type by changing the content in that variable this is what know as dynamic typing
`a={int}4`  ▶ `a={str}"hello"` 
this is ❌  not a feature thats availble in all programming languages for eample c java swift
```python
bob = 1
bob = "bob"
```
---
# HandlingError & Eceptions
try:  ▶something that acause an exception
except: ▶Do this if there was an exception
else:▶Do this if there were no exceptions
finally:▶Do this no matter what happens
```python
fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
          print(f"your index must be among 0 - {len(fruits)}\n fruit pie ")
    else:
         print(fruit + " pie")
make_pie(4)
```
---

# json

```python
with open("./data-pass.json", mode="r") as pass_list:
    data = json.load(pass_list)
    data.update(data_json)
with open("./data-pass.json", mode="w") as pass_list:
    json.dump(data_json, pass_list)
with open("./data-pass.json",mode="w") as pass_list_r:
    json.dump(data, pass_list_r, indent=4)  #indent  for reaadable
```
## Python [Tutor](https://pythontutor.com/): Visualize code in Python, JavaScript, C, C++, and Java
##  [TRIVIA](https://opentdb.com/) Free to use, user-contributed trivia question database.
##  for re run program python  every day  use  [pythonanywhere](www.pythonanywhere.com) day-32
## see [httpstatus code ](https://www.httpstatuses.org/)
