# Python Lists    [google edu](https://developers.google.com/edu/python/lists)

```Python
  list = ['larry', 'curly', 'moe']
  if 'curly' in list:
    print('yay')
```
or 
```Python
while item not in list:
  list.append(item)
```

List Methods
Here are some other common list methods.

**list.append(elem)** -- adds a single element to the end of the list. Common error: does **not return** the new list, just modifies the original.
**list.insert(index, elem)** -- inserts the element at the **given index**, shifting elements to the right.
**list.extend(list2)** or **[]+=[]** adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
**list.index(elem)** -- searches for the **given element** from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
**list.remove(elem)** -- searches for the first instance of the **given element** and removes it (throws ValueError if not present)
**list.sort()** -- sorts the list in place (does **not return** it). (The sorted() function shown later is preferred.)
**list.reverse()** -- reverses the list in place (does **not return** it)
**list.pop(index)** -- removes and returns the element at the given index. **Returns** the rightmost element if index is omitted (roughly the opposite of append()).


```python
  list = ['larry', 'curly', 'moe']
  list.append('shemp')         ## append elem at end
  list.insert(0, 'xxx')        ## insert elem at index 0
  list.extend(['yyy', 'zzz'])  ## add list of elems at end
  print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
  print(list.index('curly'))    ## 2

  list.remove('curly')         ## search and remove that element
  list.pop(1)                  ## removes and returns 'larry'
  print(list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
  ```
