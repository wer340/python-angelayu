# high order function
![high order](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-19/images/high_order_func.png)
```python
def add(n1,n2):
    return n1+n2
def multply(n1,n2):
    return n1*n2
def substracat(n1,n2):
    return n1-n2
def divison(n1,n2):
    return n1/n2
def calculator(n1,n2,operator): # when event happen function called operator
    return operator(n1,n2)

print(calculator(78,89,divison))

```
we have to bind a function that will be triggered when a particular key is pressed on the keyboard
function `as  input` in other function
`high order function` :In mathematics and computer science, a higher-order function is a function that does at least 
one of the following: takes one or more functions as arguments, returns a function as its result.
```python
from turtle import Turtle,Screen

timmy=Turtle()
screen=Screen()
def move():
    timmy.forward(100)
screen.onkey(key="f",fun=move)
screen.listen()
screen.exitonclick()
```
## construct object from blueprint
![instance](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-19/images/each_object.png)
#### it s reason have a blueprint   for constructing  many object 
each object is independt each other so in programming we would say that they are each a spararate `instance`

---
the fact that each of these object have **diffrent attributes and can be performing different methods at any one time** in programming is known
as **the state**

---
# dimension
![dimension](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-19/images/goto.png)
