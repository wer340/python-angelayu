import random
rand_seed=int(input("type a number ? "))
random.seed(rand_seed)

name=input("type your name and friend name be present ? seprate with \",\" ")
name=name.split(",")

length=len(name)-1;
loser_banker=random.randint(0,4)

print(f"{name[loser_banker]} should be pay all cost!! come on pay bill!!!")
# angela,scarllet,jenifer,margot,audrey