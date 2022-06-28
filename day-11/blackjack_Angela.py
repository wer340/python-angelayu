import random

user_cards=[]
computer_cards=[]

def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)



def calculate(computer_user_cards):
      sum_cards=sum(computer_user_cards)
      if  sum_cards==21 and  len(computer_user_cards)==2:
        return 0
    
      if 11 in computer_user_cards and sum(computer_user_cards)>21 :
        computer_user_cards.remove(11)
        computer_user_cards.append(1)
      return sum(computer_user_cards)

def compare(user_score ,computer_score) :
  if user_score==computer_score:
    return "Draw"
  elif user_score==0:
    return "win has blackjack"
  elif computer_score==0:
    return"lose comuter has blckjack"
  elif user_score>21:
    return"you went over ! Lose"
  elif computer_score>21:
    return"opponent went over you Win :)) "
  else:
    return"you Lose"
game_over=False
for _ in range(2):
  user_cards.append(deal_cards())  
  computer_cards.append(deal_cards())
  
  print(f"your cards is {user_cards}\n")
  print(f"computer cards is {computer_cards}\n")
  user_score=calculate(user_cards)
  computer_score=calculate(computer_cards)
  while game_over :
      print(f"user cards is {user_cards} and  user score is {user_score}")
      print(f" computer first card is {computer_cards[0]}")
      if user_score==0 and computer_score==0 and user_cards>21:
        game_over=True
      else:
        decision=input("if you pick card y or n ? ")
        if decision=="y":
          user_cards.append(deal_cards())
        else:
          game_over=True
while computer_score!=0 and user_cards < 17:
  computer_user_cards.append(1)
  computer_score=calculate(computer_user_cards)
print(f"user cards is {user_cards} and  user score is {user_score}")
print(f"user cards is {computer_cards} and  user score is {computer_score}")

print(compare(user_score, computer_score))