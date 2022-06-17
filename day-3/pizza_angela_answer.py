print("account pizza shop!!!")
#small pizza=$15 , medium pizza=$20 , large pizza=$25
#pepperoni s=$2   m,l=$3
#add_chesses= $1
bill=0
message="choose size your piza(small medium large) ? s or m or l ! "
size=input(message)
message="do you want pepperoni ? y or n !  "
add_pepperoni=input(message)
message="do you extra chesses ?  y or n ! "
extra_chesses=input(message)
if size=="s":
    bill+=15   
elif size=="m":
     bill+=20
elif size=="l":
     bill+=25
else:
    print("wrong value ! please be carful")
if add_pepperoni=="y":
    if size=="s":
        bill+=2
    else:
        bill+=3
if extra_chesses=="y":
    bill+=1

print(f"you pay total $ {bill}")