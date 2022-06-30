# scope  namespce  global variable

+ this concept of global and local scope doesn't just apply to variables as i alluded to before it 
 also applies to function and basically anything else you name this is a ✅consept called the namespace 
+ anything that you give a name to has a `namespace` and that namespace is valid in `certain scope`
### c++ java `block of code` have scope   but python have `not` this property
```python
#flower  my_function car brand     all of thing that called with name is a namespace
flower="rose" #global scope
def my_function(name):
    car="benz"#local scope
    flower="blue rose"
    print(flower) #output 2
    print(name)  #output 3
#print(car)#not print  beceause car in local scop
if 3>2:
    brand="apple" #global scope       #c++ java block of code have scope   but python havent this property
    print(flower) #output 1
my_function(brand)
```
## call global var
```python
enemie=2

def my_function():
    global enemie     
    enemie +=5  #refrence before assignment mean user in scope not define var  and  process on var that not define

    print(f"your enemis is local scope : {enemie}")
```
---
## whenever you give name to anything a function or a variable you have to be aware of where you created it
terrible thing local var same name with global var
## global var you are never planning on change it ever again like PI=3.14 turn into uppercase constant var in order to never chang URL="" 
```python
PI=3.14
def circle(r):
 return PI*r**2
circle(5)

```
 
