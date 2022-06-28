
import random

print("\n \n Black Jack  \n \n")

cards=[2,3,4,5,6,7,8,9,10,10,10,11]
user=[]
computer=[]
def pickup(user):
    choice=random.choice(cards)
    user.append(choice)

   
input("type any keyboard : ")
pickup(user)
pickup(user)
pickup(computer)
pickup(computer)
print(f"\n user card = {user} \n")
print(f"\n computer card = {computer} \n")
def blaackjack_loop(user,computer):
    
    sum_user=sum(user)
    sum_computer=sum(computer)
    
    if sum_user>20:
        if len(user)<3:
            if sum_user==21:
                return False
        elif sum_computer==21:
             return True
        if user.count(11)==1:
            index=user.index(11)
            user[index]=1
            sum_new_user=sum(user)
            if sum_new_user>21:
                return False
            else :
                return "continue"
        else:
            return False
    elif sum_computer>21 :
        if computer.count(11)==1:
            index=computer.index(11)
            computer[index]=1
            computer_new_user=sum(computer)
            if computer_new_user>21:
                return True
            else :
                return "continue"
        else:
            return True
    else:
        return None





if  blaackjack_loop(user,computer)==False:
    print("you lose")
elif  blaackjack_loop(user,computer)==True :
    print("you win")
else:
    while blaackjack_loop(user,computer)==None:
        ask_user=input("whether you pick card or? y or n :" )
        if ask_user=="y":
                input("type any keyboard ")
                pickup(user)
                print(f"\n user card = {user} \n")
                print(f"\n computer card = {computer} \n")
                blaackjack_loop(user,computer)
                if blaackjack_loop(user,computer)==True:
                            print("you win")
                elif blaackjack_loop(user,computer)==False:
                            print("you lose")
        else:
                while blaackjack_loop(user,computer)=="continue":
                        pickup(computer)
                        print(f"\n computer card = {computer} \n")
                        blaackjack_loop(user,computer)
                        if blaackjack_loop(user,computer)==True:
                            print("you win")
                        elif blaackjack_loop(user,computer)==False:
                            print("you lose")

# user_deciton=True         
# while user_deciton:    
#     ask_user=input("whether you pick card or? y or n :" )
#     if ask_user=="y":
#         input("type any keyboard ")
#         pickup(user)
#         print(f"\n user card = {user} \n")
#         print(f"\n computer card = {computer} \n")
#         blaackjack_loop(user,computer)
#         if sum(user)>21 or sum(computer)>21:
#           user_deciton=False
#     else:
#         user_deciton=False
# computer_deciton=True
# while computer_deciton:
#     if sum(user)>21 or sum(computer)>21:
#         computer_deciton=False
#     else:
#         pickup(computer)
#         print(f"\n computer card = {computer} \n")
#         blaackjack_loop(user,computer)

print("\n Game Finish")