from ctypes import windll
import random
scissors=''''
     ______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

number=int(input("Scissors,Rock,Paper game ? type 0 for rock ,type 1 for paper,type 2 for scissors ? "))

my=[rock,paper,scissors]
my_choice=my[number]
print(my_choice)
machine=random.randint(0,2)
machine_choice=my[machine]
print(f"computer choose : \n {machine_choice}")

# state=[[rock,scissors],[paper,rock],[scissors,paper],[paper,scissors],[rock,paper],[scissors,rock],[scissors,scissors],[paper,paper],[rock,rock]]
win=[[rock,scissors],[paper,rock],[scissors,paper]]
lose=[[paper,scissors],[rock,paper],[scissors,rock]]
equal=[[scissors,scissors],[paper,paper],[rock,rock]]
if   my_choice==machine_choice:
     print("you equal please try again")
elif win.count([my_choice,machine_choice])==1:
     print("you win")
else:
     print("you lose")