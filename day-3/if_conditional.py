print("whether can rollercoaster ride or not??")
height=int(input ("enter your height(cm) ? "))
if height>=140:
 #nested to if   you can more elif condion
    #elif condition1 accept break althuth next condition 
    message="enter your age ? "
    age=int(input(message))
    if age<=12:
         message="you pay $5  "
         print(message)
    elif age<=18:
        message="you pay $7  "
        print(message)
    elif age<30:
        message="you pay $12  "
        print(message)
    else:
        message="you pay $18  "
        print(message)
else:
    message="you cant ride  sorry about :(("
    print(message)