# path

 ---
 
## snake game High_score

---



path and dictionary  read and write file like a word  office   a use mechanizm  for store  data

```python
file = open("scarlett.txt",encoding="utf8" ,errors="ignore")
shows_txt = file.read()
print(shows_txt)
file.close()

```

other way self close  after process done 
```python
with open("Jennifer_Lawrence.txt",mode="w") as book:   
    book.write(""
               "Jennifer Lawrence born on August 15, 1990,\n in Indian Hills, Kentucky, United States, is an American film"
               "\n actress who primarily works in Hollywood films.")
 ```
 
 # mode   r
 
 |mode|do|
 |----|---|
 |r|read|
 |w|write|
 |rb|read binary|
 |a|append|
 
