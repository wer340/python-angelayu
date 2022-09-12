# HandlingError & Eceptions

## four keyworl thats important for haandling exception
### try:  ▶something that acause an exception
### except: ▶Do this if there was an exception
### else:▶Do this if there were no exceptions
### finally:▶Do this no matter what happens

```python
def search():
    website = website_i.get()
    try:
        with open("./data-pass.json") as passlist:
            data = json.load(passlist)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="no any data a for search")
    else:
        try:
            record = data[website]
        except KeyError:
            messagebox.showinfo(title="Error",
            message=f"⛔ dont exist '{website}'  password in password list")
        else:
            password = record["Password"]
            email = record["Email"]
            messagebox.showinfo(message=f"Email:   {email} \n Password :  {password} \n ")
```

## raising exceptions
raise keyword  this allows us to do is to raaise our own exceptions
thrown a  error   made up  by yourself
raise ValueError("human height should not be over 3 meter")

```python

height=float(input("inter your height meter ? : "))
if height>3:
    raise ValueError("your height shouldn't be over 3 meter")
    print("wrong")
weight=float(input("inter your weight kg ? : "))
bmi=weight/height**2
bmi=round(bmi,2)
print(f"your bmi is {bmi}")
# raise TypeError("belaaa")
```

# json
## `j`ava`s`cript `o`bject `n`otation


```python
import json
open(.json,mode="w")
```
write > `json.dump(object,data_file(openjson),indent=4)` ▶mode="w" ✅indent for easy to read \
read > `json.load(data_file)`▶ mode="r"\
update > `json.update() `▶mode="r"like append  1️⃣  first json load or json dump 2️⃣  then json update\
so essentioly we can use `json.dump` and `json.load` to serialize and deserialiaze to python dictionaries\
and allows us that free interchange of information\
![try](https://github.com/wer340/python-angelayu/blob/main/day-30/image/json.png?raw=true)
