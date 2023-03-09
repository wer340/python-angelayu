# snake game

![snakeGame](https://raw.githubusercontent.com/wer340/python-angelayu/main/21_day-21/iamges/breakpoint.png)

## class inheritance modify class and give more capability

---
![inherit](https://raw.githubusercontent.com/wer340/python-angelayu/main/21_day-21/iamges/defInherit.png)
its process of inheriting behavior and appearance from an existing class is known as class inheritance 
not only can inherit appearance but we can also inherit behavior 
how can define
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

----

now in order to get fish class to inherit from another class all we have to do add a set of parentheses after the name of the class 
and then in order to get a hold of everthing that an animal has is so its attributes and methods all we have to do is inside the init
add this `super().__init__()`  and the super refer to the `superclass`  initial everything that the super class can do in our fish
two part[(Animal),(super().__init__())] allow to inherte all atributes and methods
what it allows us to do is to take an existing aclass that we have created 

## turtle function
distance method measure distance between own instance till inastance given inside pranthess
```python
turtle.head.distance(other_instance)
```

----

# slicing
![slicing](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-21/iamges/slicinga.png)
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
# shift 
![list](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-21/iamges/list.png)
