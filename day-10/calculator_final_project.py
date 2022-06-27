


# add
from typing import final


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
    
num1=int(input("whats first number ? : "))
num2=int(input("whats second number ? : "))
for key in operator:
    print(key)
operator_in=input("whats operator ? : ")
def function_call(operator_in):
    """give a sign opration give a function calc"""
    for key in operator:
        if operator_in==key:
            function_symbol=operator[key]
            return function_symbol 

def calculator(num1,num2,operator_in):
    func=function_call(operator_in)
    final=func(num1,num2)
    print(f"{num1} {operator_in} {num2} = {final}")
    calc_flag=True
    while calc_flag:
        decion=input("are you continu to calc ? y or no")
        if decion=="n":
            return "calc finish"
        elif decion!="y":
            print ("invalid number")
        operator_in=input("whats operator ? : ")
        num2=int(input("whats other number ? : "))
        
        print(f"{final} {operator_in} {num2} = {func(final,num2)}")
        final=func(final,num2)
calculator(num1,num2,operator_in)