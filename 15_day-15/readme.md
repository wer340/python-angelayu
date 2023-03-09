##  caffe machine
```python
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True
```
## me solution ☹
```python
def is_resource_sufficient(model, resources):
    global MENU
    water = MENU[model]['ingredients']['water']
    coffee = MENU[model]['ingredients']['coffee']
    if model == "espresso":
        milk = 0
    else:
        milk = MENU[model]['ingredients']['milk']
    if resources["water"] > water and resources['coffee'] > coffee and resources['milk'] >= milk:
        resources['water'] -= water
        resources['coffee'] -= coffee
        resources['milk'] -= milk

        return True
    else:
        return False
 ```
# IDE
### intelligent Development Enviroment
#pycharm 
pycharm  its feature advance  property   
#### Built-in linter > automaticly applies thoes rule and guidaance to our code but not effect your code only suggestion for readable
![pycharm_3](https://raw.githubusercontent.com/wer340/python-angelayu/main/15_day-15/image/pycharm3_linter.png)
https://peps.python.org/pep-0008/  style guide 
another advance feature  is   loacl history and revert time back 
another handy feature structure   all of variable  all of function
------
https://www.jetbrains.com/pycharm/download/#section=windows   free version
![ide type](https://raw.githubusercontent.com/wer340/python-angelayu/main/15_day-15/image/ide.png)
![pycharm_1](https://raw.githubusercontent.com/wer340/python-angelayu/main/15_day-15/image/pycharm_feaature.png)
![pycharm_2](https://raw.githubusercontent.com/wer340/python-angelayu/main/15_day-15/image/pycharm2.png)

