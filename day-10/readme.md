# function output

#### when the computer encounters a line that has the word `return` on it then it knows ✅that this line is the end of the function

```python
def my_function():
  word="hello world"
 return word.title()
  ```
[function](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-10/image/outputaa_function.png)

# docstring
[docstring](https://raw.githubusercontent.com/wer340/python-angelayu/main/day-10/image/docstring.png)
##### has to go as the first line after the declartion  thre qutation mark """a="string" """
```python
def my_function():
""" this function return a word title """
  word="hello world"
 return word.title()
 ```
 ### diffrence  💎print and 💎return
### return  can be used first output as input at second cycle function

# recursion
#### recursion, a function reuse in same function ❌be careful in order to infinite loop
```python
def my_function():
  word="hello world"
  my_function()   #❌ make infinite loop this example 
  ```
