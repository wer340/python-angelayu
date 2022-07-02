import logo
from data import data
import random
print(logo.logo)


def pick_list():
    
   return (random.choice(data))   # () You need to use parentheses

def print_inf(a,b):
    global score
    score +=1
    print (f'\n you win  A follower_count : {a["follower_count"]} \n B follower_count : {b["follower_count"]} \n')
    


game_over=False
score=0
a=pick_list()
b=pick_list()
while not game_over:
    
    print(f'compare A : {a["name"]}, a {a["description"]} from {a["country"]} \n')
    print(logo.vs)
    print(f'\n compare B : {b["name"]}, a {b["description"]} from {b["country"]} \n')

    answer=input("who has more followers? 'A' or 'B' : ")
    if answer=="a" and a["follower_count"]>b["follower_count"]:
        print_inf(a,b)
        b=pick_list()
        
    elif answer=="b" and a["follower_count"]<b["follower_count"]:

          print_inf(a,b)
          a=pick_list()
    else:
         print (f'\n you Lose  A follower_count : {a["follower_count"]} \n B follower_count : {b["follower_count"]} \n')
         game_over=True

print(f"you lose Your final score : {score}")