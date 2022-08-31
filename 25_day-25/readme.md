# pandas module  powerful
#### how can read and analize them  `csv`  `c`omma `s`eprated `v`alue  
csv are a very common way of representing  taabula data like spreedsheet
 when open  csv  pretty painful to work with data  which all string format seprated with commas
take alot of cleaning 🥱😭to actually be able to extract each column
```python
with open("./wheather_sheet.csv") as wheather:
    data=wheather.readlines()

    print(data)
 ```
python lang thats used realy heaavily for adata processing data analysis there s alot of great tools
for working with tabula data

---
# 📈import csv ✅ library 
```python
import csv
with open("./wheather_sheet.csv") as wheather:
    data=csv.reader(wheather) #create object
    temperture=[]
    for row in data:
        if row[1]!="temp":
            temperture.append(int(row[1]))

    print(temperture)
```
####  csv number cant read  int   deafult string this issue for  alot row and data  cause so much  faff🥱   

---
# pandas   lib ☕ super helpful super powerful data analysis 

install package `pip install pandas`
```python
import pandas
import math
with open("./wheather_sheet.csv") as wheather:
    data = pandas.read_csv(wheather)
    print(type(data)) #get all data   expect <class 'pandas.core.frame.DataFrame'>
    print(type(data["temp"])) # get a column  expect  <class 'pandas.core.series.Series'>
```

# data structure   2 overall stracture     series  and dataFrame
 data frame kind of equivalent of your `whole table` here 
 so every single sheet inside an excel file or inside a google sheet file would be considered a data frame
 series is baasicly equivalent to a list it s kind of a `single column` in your table 


---
# 2way for fetch column 
### 1️⃣data.namecol ✅ this way  avoid of mistake 
### 2️⃣data["aname_col"]✅

---
##  how fetch a record  [row data]  data[day.day=="monday"]  return row
⛔⛔filename  not name module  like `pandas.py`⛔⛔⛔⛔⛔⛔⛔

# useful method pandas
```python
city_inf = data[data["state"] == answer] #get a row with this propert
texter.write(city_inf.state.item()) # item() just return value 
pd_aaverage=data["temp"].mean() #average column
#create data frame
dict_actress={
 "name":["scarlett"], #value key termof []
 "lName":["johansson"]#value key termof []
}
data=pandas.DataFrame(dict_actress)
```

# get cordinate from image
```python
def get_cordinate(x, y):
    print(x, y)
turtle.onscreenclick(get_cordinate) #to callback function is passed argumet x , y
```
