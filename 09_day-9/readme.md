# dictionary and nesting 

## line of program instructions for the computer and dictionaries are really useful allow group together tag realated a piece of information

![dictonary](https://raw.githubusercontent.com/wer340/python-angelayu/main/9_day-9/image/dictonarya.png)

# best to do ✅first key at next line    

![besttodo](https://raw.githubusercontent.com/wer340/python-angelayu/main/9_day-9/image/besttodo.png)

```python
#{key:value}  
dictionary={"bug" : "an error in a program ..","function":"A piece of code taht you can "} 
print(dic["bug")]#output "an error in a program .."
#❌key spell   by developer key error   ❌bog >bug✅

#second error key without "" Quotation  
dictionary={bug : "an error in a program ..",function:"A piece of code taht you can "}
```
# adding new item to dictionary
```python
dictionary={} #if {} give a dictionary this value  clear all data 
#add new record
dictionary["loop"]="The action of doing something over ..."
```
# loop for dictionary 
```python
dictionary={"bug" : "an error in a program ..","function":"A piece of code taht you can "} 
for thing in dictionary:#thing is key 
	print(thing) # output key
	print(dictionary[bug])#output an error in a program ..
  ```
  
# nesting
```python
list_actress=[
{"Scarlett Johansson":{
    "movies":["Avengers: Endgame","Lost in Translation","Her","The Avengers","Ghost World"],"age":38}
},
{"Sharon Stone":["Basic Instinct","Casino,The Quick and the Dead","Sliver"]},
{"Jennifer Connelly":["A Beautiful Mind","House of Sand and Fog","Requiem for a Dream","The Rocketeer"]},
{"Brooke Shields":["The Blue Lagoon","Pretty Baby","Wanda Nevada","The Midnight Meat Train"]},
{"Monica Bellucci":["Malena","The Matrix Revolutions","The Matrix Reloaded","Shoot 'Em Up"]}
]

print(list_actress[0]["Scarlett Johansson"]["movies"][4]) #Ghost World 
print(list_actress[1]["Sharon Stone"][2])#Casino

list_actress.append({"Audrey Hepburn":["Breakfast at Tiffany's","Roman Holiday","Charade","My Fair Lady"]})
print(list_actress[5])
```
## Python [Tutor](https://pythontutor.com/): Visualize code in Python, JavaScript, C, C++, and Java
![data srtucture](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-9/image/Visualize%20png.png)

## how do we if don't knows keys and values analyze this {key:value} ✅✔solution for key in return
```python
import random
list_dictionary=[
{"Scarlett Johansson":"Avengers: Endgame"},
{"Sharon Stone":"Basic Instinct"},
{"Jennifer Connelly":"A Beautiful Mind"},
{"Brooke Shields":"The Blue Lagoon"},
{"Monica Bellucci":"Malena"}
]
my_choice=random.choice(list_dictionary)
#how can analyze a {key:value}
for key in my_choice:
	print(key)
	print(my_choice[key])
```
