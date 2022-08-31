# list and dict comprehension ☕💎

## List

list comprehension thing   that  not have been seen other language
less  write code ☕
first one item of list itrate then by if consitional is tested  and passed to first place  
```python
names = ['Scarlett Johansson', 'Jennifer Lawrence', 'Emma Watson']           
new_list=[name.replace(" ","_") for name in names if len(name)<15]
```
## Dict
dictonary also  due to  list comprehensaion   (key,value) convert tuple  and  in dictionary also each (key,value) convert tuple  by `itemes()` method

```python
students = ['Scarlett Johansson', 'Jennifer Lawrence', 'Emma Watson']      
dict_students = {student: randint(1, 100) for student in students}  #sitution1️⃣list to dict 
dict_best_students={student:score for (student,score) in dict_students.items() if score>30 } #sitution2️⃣dict to new dict
```

## pandas
in pandas modulas also  can through each rows make loop  that  iterrows() method

```python
import pandas
data=pandas.read_csv("./wheather_sheet.csv")
#loop through row   use Dataframe.iterrows()
for (key,value) in data.iterrows():
    print(key)
    print(value.codition
```
![panda](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-26/image/loopRows.png)
