
import random

# print("\n \n Black Jack  \n \n")

# cards=[2,3,4,5,6,7,8,9,10,10,10,11]
user=[]
computer=[]
def pickup(user):
    choice=random.choice(cards)
    user.append(choice)

   
# input("type any keyboard : ")
# pickup(user)
# pickup(user)
# pickup(computer)
# pickup(computer)
user=[10,4]
computer=[2,3]
print(f"\n user card = {user} \n")
print(f"\n computer card = {computer} \n")
def is_ace():
    if len(user)==2 and sum(user)==21:
        return False
    else:
        return True
def blaackjack_loop(user,computer):
    if not is_ace():
        return False
    elif sum(user)>21:
        return False
    elif sum(computer)>21 :
        return True
  


answer=blaackjack_loop(user,computer)


if  answer==False:
    print("you lose")
elif  answer==True :
    print("you win")
else:
    while answer==None:
        ask_user=input("whether you pick card or? y or n :" )
        if ask_user=="y":
                input("type any keyboard ")
                pickup(user)
                print(f"\n user card = {user} \n")
                print(f"\n computer card = {computer} \n")
                answer=blaackjack_loop(user,computer)
                if sum(user)>sum(computer) and answer==None:
                            break
        else:
                while answer==None:
                        pickup(computer)
                        print(f"\n computer card = {computer} \n")
                        answer=blaackjack_loop(user,computer)
                        if sum(user)<sum(computer) and answer==None :
                            answer=False
                            break 

if  answer==False or sum(user)<sum(computer) :
    print("you lose")
elif  answer==True or sum(user)>sum(computer) :
    print("you win")                      

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