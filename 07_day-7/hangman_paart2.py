import random
word_list=["ardvark" , "baboon" ,"camel"]

select=random.choice(word_list)
print(select)
word_shape=[]
for char in range(0,len(select)):
    word_shape.append("_")
for _ in select:
    word_shape+="_"
letters=input("please enter your letter? ")
i=0
for item in select:
    if item==letters:
        word_shape[i]=item
    
    i+=1
print(word_shape)