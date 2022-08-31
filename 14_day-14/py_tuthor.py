
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    }]
import random


def pick_list(n):
    
   return (data[n])   # () You need to use parentheses

def print_inf(a,b):
    global score
    score+=1
    print (f'\n you win  A follower_count : {a["follower_count"]} \n B follower_count : {b["follower_count"]} \n')
    


game_over=False
score=0
a=pick_list(1)
b=pick_list(3)
while not game_over:
    
    print(f'compare A : {a["name"]}, a {a["description"]} from {a["country"]} \n')
   
    print(f'\n compare B : {b["name"]}, a {b["description"]} from {b["country"]} \n')

    answer=input("who has more followers? 'A' or 'B' : ")
    if answer=="a" and a["follower_count"]>b["follower_count"]:
        print_inf(a,b)
        b=pick_list(5)
        
    elif answer=="b" and a["follower_count"]<b["follower_count"]:

          print_inf(a,b)
          a=pick_list(7)
    else:
         print (f'\n you Lose  A follower_count : {a["follower_count"]} \n B follower_count : {b["follower_count"]} \n')
         game_over=True

print(f"you lose Your final score : {score}")