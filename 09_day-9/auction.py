import os
import logo
people_chain=True
list={}
big_price=0
winner=""
while people_chain:
    os.system('cls')
    print(logo.logo)
    name=input("please enter your name : ")
    price=int(input("please enter your price for auction : $ "))
    list[name]=price
    auction_time=input("weather auction continue or no ? y or n " ).lower()
    if auction_time=="n":
        people_chain=False

for key in list:
    if list[key]>big_price:
        big_price=list[key]
        winner=key
print(f"{winner} win this aauction with $ {big_price}")