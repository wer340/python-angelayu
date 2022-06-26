


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
    result=round(a/b,6)
    return result

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
            function=operator[key]
            return function 

def calculator(num1,num2):
    func=function_call(operator_in)
    return func(num1,num2)
final=calculator(num1,num2)
print(f"{num1} {operator_in} {num2} = {final}")