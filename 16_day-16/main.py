import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_maker.report()
money_machine.report()
menu = Menu()
menu_item=MenuItem

item = menu.get_items()
name = input(f"give type caffe {item}  ? : ")

