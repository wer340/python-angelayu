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
or this class empty** ✔ `we can use keyword pass` and all it does is it just passes it says i dont want to have a go right now just continue to the next line of code 
AND THIS GET RID OF OUR ERROR both in the function as well as  in our class declaration 
