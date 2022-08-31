import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
number=range(0,10)
symbols=["!","#","$","%","&","(",")","*","+"]
print("Welcom to the password generator")
nr_letters=int(input("how many letters would you like in your password?\n"))
nr_symbol=int(input("how many symbolas would you like in your password?\n"))
nr_numbers=int(input("how many numbers would you like in your password?\n"))
letters_final=""
#esay level
for item in range(0,nr_letters):
    chance=random.randint(0,51)
    letters_final+=letters[chance]

for item in range(0,nr_symbol):
    chance=random.randint(0,8)
    letters_final+=symbols[chance]

for item in range(0,nr_numbers):
  letters_final+=str(random.randint(0,9))

print(f"your passwors is  {letters_final}")