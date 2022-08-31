import random
NUMBER=random.randint(1, 100)

print(" guess number  1,100  please select your level: ")
level=input("\n \n hard level or easy level : hard or easy ? : " )


def guess(attemp):
    for index in range(attemp):
        choice=int(input("guess number ?  : "))
        if choice<NUMBER:
            print(f"number is low you have {(attemp-1)-index} chance  ")
        elif choice>NUMBER:
            print(f"number is high you have {(attemp-1)-index} chance")
        elif choice==NUMBER:
            print(f"congrudulation you guess correctwith {(attemp-1)-index} chance remain")
            return "you win"
        elif (attemp-1)-index==0:
           return "you lose "

if level=="hard":
    guess(5)
else:
    guess(10)

print(NUMBER)