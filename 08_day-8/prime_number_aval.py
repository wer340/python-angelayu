import os
import math
os.system('cls')
number=int(input("enter your number for prime checker : "))
#(2^n)-1    n prime




def prime_checker(number):
    num=math.ceil(math.sqrt(number))  
    is_prime=True 
    for item in range(2,num) :
        if number%item==0:
            is_prime=False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
         


prime_checker(number)