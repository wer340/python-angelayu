# path

 ---
 
## snake game High_score

---



path and dictionary  read and write file like a word  office   a use mechanizm  for store  data

```python
file = open("scarlett.txt",encoding="utf8" ,errors="ignore") # encoding for else english lang   errors optional
shows_txt = file.read()
print(shows_txt)
file.close()

```

other way ✅self close  after process done 
```python
with open("Jennifer_Lawrence.txt",mode="w") as book:   
    book.write(""
               "Jennifer Lawrence born on August 15, 1990,\n in Indian Hills, Kentucky, United States, is an American film"
               "\n actress who primarily works in Hollywood films.")
 ```
 # why do you need close 🕷
+ once python open the file it basiclly take up some of resource of your copmuter at some point later on it might adecide to close it
and free up those resources so instad  we are going to tell it to close down  the file manually this line of code
similar consept  alot lots lots of tab in chrome browser 
write()  before open(mode="w")  deafult mode="r"   mode="a
 # mode   
 
 |mode|do|
 |----|---|
 |r|read|
 |w|write|
 |rb|read binary|
 |a|append|
 
 ----
 
 # absolute file path  start with  root     path relative raealate with root ./file ~ file(shorten)
 ### /users/name/desktop/....  static                       
 ![path](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-24/images/path.png)
 
 ----
 
 # important ⛔⛔⛔⛔⛔
 ## one of pecularity about file path in windows  and mac  is that in mac each of folder are seprated by a `/`✅[forwardslash] whereas on windows
## they seprated by a `\` ✅backslash  as you notice
## ⛔🕷when we are writing python code we ✅💎dont care about that   we can just write it as `/`[forward slash] and making sure that we have the root
## which represents the c drive so thid entire part 
 ![win](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-24/images/pathwinmac.png)

----
method 
[replace](https://www.w3schools.com/python/ref_string_replace.asp) 
[strip](https://www.w3schools.com/python/ref_string_strip.asp)  ~ trim javascrip 
[readlines](https://www.w3schools.com/python/ref_file_readlines.asp) ~ return each line  as a array of list
