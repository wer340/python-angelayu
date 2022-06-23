import random
word_list=["ardvark" , "baboon" ,"camel"]

select=random.choice(word_list)
print(select)
word_shape=[]

for _ in select:
    word_shape+="_"
End_Of_Game=False
while not End_Of_Game:
    letters=input("please enter your letter? ")

    for i in range(len(select)):
        item=select[i]
        if item==letters:
            word_shape[i]=item
        
    print(word_shape)
    if "_" not in word_shape:
        End_Of_Game=True
print("You Win.")