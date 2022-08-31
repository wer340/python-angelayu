import random
#The seed() method is used to initialize the random number generator.
#The random number generator needs a number to start with (a seed value), to be able to generate a random number.
#By default the random number generator uses the current system time.
#Note: If you use the same seed value twice you will get the same random number twice. See example below
test_speed=int(input("type a number ?  "))
random.seed(test_speed)#whatever  more the more ranging is involved as a result
rand=random.randint(0,1)
if rand==0:
    print("Tails")
else:
    print("Heads")

# print(f"your seed number is {number}")