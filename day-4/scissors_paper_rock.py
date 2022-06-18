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
print(my[number])
machine=random.randint(0,2)
print(f"computer choose : \n {my[machine]}")

