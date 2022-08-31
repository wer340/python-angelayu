MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_resource(data):
    print(f"\nwater : {data['water']}\n milk:{data['milk']}\n coffee:{data['coffee']}")


def input_type(name):
    if name == "ex":
        return "espresso"
    elif name == "la":
        return "latte"
    else:
        return "cappuccino"


#

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


def coin_process(model):
    cost = MENU[model]['cost']
    quarter = int(input("how many quarter"))
    dimes = int(input("how many dimes"))
    nickle = int(input("how many nickle"))
    peny = int(input("how many peny"))
    total_coin = (0.25 * quarter) + (0.10 * dimes) + (0.05 * nickle) + (0.01 * peny)
    if total_coin > cost:
        print(f"here is {total_coin - cost} change")
        print(f"here is {model}")
        return cost
    else:
        print("your money low")


def caffe_machine(resources):
    fund = True
    while fund:
        print_resource(data=resources)
        name = input("please select type of coffee : espresso  [ex], latte [la], cappuccino [ca]")
        name = input_type(name)
        if is_resource_sufficient(model=name, resources=resources):
            coin_process(name)

        else:
            print("refund your worth")
            fund = False


caffe_machine(resources=resources)
# todo : 3 coin process
# todo :4  check transaction

# todo:5 make cafe  accumulate money
