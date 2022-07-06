# GUI Graphical User Interface
turtle module graphic
how do i know to do that? is it becaause iam super experienced i super clever  ?   not
the way that programmers go about figuring out how  to use these modules or packages is through the ✅use of documention 
way: when documention is long    `search your subject in google +stackoverflow`
```python
import turtle as t #✅
from random import choice

timmy=t.Turtle() 
t.colormode(255)
screen=t.Screen()
timmy.speed()

timmy.setheading(225) #set angle    1/4 2/4 3/4 4/4  between 180-270 > 225 :)) after draw count dot *50 =8*50=400 
timmy.forward(400)
timmy.setheading(0)
for _ in range(10):
    
    timmy.forward(50)
    timmy.dot(20,"red")

screen.exitonclick()  # screen not close ✅

```
# [heros](https://pypi.org/project/heroes/) module  random name generate
```python
import heroes
list=[]
for _ in range(5):
    list.append(heroes.gen())
print(list) #['Monstress', 'Rachel Grey', 'Logan', 'Bart Rozum', 'Free']
```
### (1,2,3)a `data type`  it has round brackets around it and then each of the item inside are separated by a comma
doesnt it not look a like bit a list [1,2,3]   
**whats diffrence with list ?**
a `tuple` is going to be `carved in stone` 
✅so you cant change the value like you can with list  ✔💎immutable
why would you use of tuple  a constant list sort of list 
```python
my_tuple=(1,2,3) 
my_tuple[0]=1
list(my_tuple) #convert to list
```

# [colorgram](https://pypi.org/project/colorgram.py/) module extract color from image
```python
import colorgram
colors=colorgram.extract("Image/colorgram.jpg",5)
color_rgb=[]
for color in colors:
    r=color.rgb.r    
    g=color.rgb.g
    b=color.rgb.b
    tuple_color=(r,g,b) 
    color_rgb.append(tuple_color)  
print(color_rgb) #[(246, 242, 235), (247, 241, 244), (239, 242, 247), (237, 245, 240), (215, 148, 91)]
```

[rgb color ](https://www.w3schools.com/colors/colors_rgb.asp)
