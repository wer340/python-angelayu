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
