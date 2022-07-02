import logo
from data import data
import random
print(logo.logo)


def pick_list():
    num=random.randint(0,3)
    return random.choice[num]




game_over=False
score=0
while not game_over:
    a=pick_list()
    b=pick_list()
    print(f'compare A : {a["name"]}, a {a["description"]} from {a["country"]} \n')
    print(logo.vs)
    print(f'\n compare A : {b["name"]}, a {b["description"]} from {b["country"]} \n')

    answer=input("who has more followers? 'A' or 'B' : ")
    if answer=="A" and a["follower_count"]>b["follower_count"]:
        print ("you win")
        score+=1
    elif answer=="b" and a["follower_count"]<b["follower_count"]:

         print ("you win")
         score+=1
    else:
        game_over=True

print("you lose")