print("whether can rollercoaster ride or not??")
height=int(input ("enter your height(cm) ? "))
bill=0
if height>=140:
 #nested to if   you can more elif condion
    #elif condition1 accept break althuth next condition 
    message="enter your age ? "
    age=int(input(message))
    if age<=12:
         message="you pay $5  "
         print(message)
         bill+=5
    elif age<=18:
        message="you pay $7  "
        print(message)
        bill+=7
    elif age<30:
        message="you pay $12  "
        print(message)
        bill+=12
    elif age>45 and age<55: #&=and
        bill=0
        message=f"you total pay {bill}  "
        print(message)
    
    else:
        message="you pay $18  "
        print(message)
        bill+=18
   
    wants_photo=input("are you wanna photo taken($3)? y or n ")
    if wants_photo=="y" :
        bill+=3
        message=f"you total pay {bill}  "
        print(message)
    else:
        message=f"you total pay {bill}  "
        print(message)
   
else:
    message="you cant ride  sorry about :(("
    print(message)