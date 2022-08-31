import random
word_list=["ardvark" , "baboon" ,"camel"]
number=random.randint(0,3)
select=word_list.pop(number)
print(select)


letters=input("please enter your letter? ")
for item in select:
    if item==letters:
        print("right")
    else:
        print(False)