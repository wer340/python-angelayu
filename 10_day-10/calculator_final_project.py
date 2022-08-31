import os
import logo

# add

def add(a,b):
    return a+b
# subtract
def subtract(a,b):
    return a-b
# multiply
def multiply(a,b):
    return a*b

#divide
def divide(a,b):
        return a/b

operator={
    "+":add ,
    "-":subtract ,
    "*":multiply ,
    "/":divide 
}
    

def function_call(operator_in):
    """give a sign opration give a function calc"""
    for key in operator:
        if operator_in==key:
            function_symbol=operator[key]
            return function_symbol 

def calculator():
    os.system('cls')
    print(logo.logo)
    num1=float(input("whats first number ? : "))
    calc_flag=True
    while calc_flag:
        num2=float(input("whats second number ? : "))#input int2
        for key in operator:
            print(key)   #print symbol
        operator_in=input("whats operator ? : ") #input symbol
        func=function_call(operator_in)
        final=func(num1,num2)
        print(f"{num1} {operator_in} {num2} = {final}")
        decion=input("are you continu to calc ? y or n ")
        if decion=="n":
            calc_flag=False
            calculator()
        elif decion!="y":
            print ("invalid number")
        else:
            num1=final
        
        
calculator()