# oop   create class
+ how actually class
----------------------
you have the `class keyword` followed by the name of your class and  then a semicolon and then all of the code thats in your class 
will follow this and it will be
![class](https://github.com/wer340/python-angelayu/blob/main/day-17/image/class.png?raw=true)
-------------
 when🔽 
```python
class User:
		# ERROR
user_1=User()
def function():
	 	# ERROR
print("hello")
```
🔼now we get an error here👆 because theres an `indent expected` so basically **python** `doesnt like` it when `you cereate` something like a class or 
when you create something like a function and you `have a semi colon` but you dont have **anything inside** that functional class 
```python
class User:
	pass	#THIS GET RID OF OUR ERROR
user_1=User()
def function():
	pass    #THIS GET RID OF OUR ERROR
print("hello")
```
if i just immediately wanted to print hello afterward  i get exactly the same error ; `indent expected` its expected this function `you have created function  or this class`
you have created to have some sort of content before you `go head and do something` else so how can we `fix` this ? well  **if we actually realy want to leave this function 
or this class empty** ✔ `we can use ## keyword pass ##` and all it does is it just passes it says i dont want to have a go right now just continue to the next line of code 
AND THIS GET RID OF OUR ERROR both in the function as well as  in our class declaration 
--------------------
## constructor
how do we `create attribute` for class
one of the easiest way of doing this is simply tapping into your object and then adding an attribute
and we could add aas many attributes as we want just by using this method of `using the dot notation` after the `name` of the object
and then just `adding` any piece of data we want 
#### reminder : attribute is a variable thats associated with an object
```python
class User:
	pass	
user_1=User()
user_1.id="001"
user_1.username="scarlett"
print(user_1.username)
```
###  question  ?
we had `lots and lots of` attributes like this and every single time we create a new user 🔽
```python
class User:
	pass	
#1	
user_1=User()
user_1.id="001"
user_1.username="scarlett"
#2
user_2=User()
user_2.id="002"
user_2.username="emilia"
#3
#statement
#4
#statement
#....
```
this is a little bit `prone` to `error` because 
**so is there a way of making thid simpler?**
how can i `specify` all these starting piece of information when i create my object from the class ?
in order to do this  we have to understand something called a ✔`constructor`   which is a `part of the blueprint` that `allow` us
to `specify` what should happen when your object is being constructed this is also known in progaramming as `initializing` an object
when the object is being initialized we can set variable or counter to they are starting value in python
----------
![constructor](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-17/image/set_attribute_constructor.png)
---------
the way that we would create the `constructor` is by using a special function  which is the init function ✔✅✅📗
you can tell its `special` because it `isnt` just `def keyword` and then the name of the function its got `two underscore either side` of the name 
and this `means` that is a method athat the `python interpreter knows` about and knows that it has a `special function` 
what is the special function ? well its normally used to initialize the attributes
```python
class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
 
user_1 = User("001", "Scarlett")
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Scarlett"
```
inside this init function is where we `initialize` or `create` the starting vlaue for attributes 
the important thing to remember is that the init function is going to be called every time you create a new object from this class
===============
![runeverytime](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-17/image/init_called.png)
=============
### remider : attribute  are the thing that the object will have and they are basically just `variables` that are associated with the final 
```python
class User:
    def __init__(self, id, username):
    	pass
```
in addition to this ✅called self  which is the actual object thats being created or being initialized
and that parameter is going  to be passed in when an object gets constructed from this class and once you recive that data 
you can use it to set the object atrributes
```python
class User:
    def __init__(self, id, username,follower):
        self.id = id
        self.username = username
         self.followers =follower
user_1 = User("001", "Scarlett",0)
```
but it doesnt make sense for all attributes to be initialized when we actually create our object so if for example
in our case👆👆so in python we can also `provide a default value`
Instead of setting it equal to one of the parameter that's being passed in when this class is being initialized,  instead I'm just setting it to a value
```python
class User:
class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
user_1 = User("001", "Scarlett")

```
