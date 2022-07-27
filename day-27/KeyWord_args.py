
def calculator(n,**num):
    n+=num.get("add")
    n*=num["mutiply"]
    return n


print(calculator(3,add=8,mutiply=2))