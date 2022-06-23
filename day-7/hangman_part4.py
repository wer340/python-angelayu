import random
import hangman_shape
word_list=["ardvark" , "baboon" ,"camel"]

select=random.choice(word_list)
print(select)
word_shape=[]

for _ in select:
    word_shape+="_"
End_Of_Game=False
i=0
while not End_Of_Game:
     letters=input("please enter your letter? ")
     if letters not in select:
        print(hangman_shape.hangman_pics[i])
        i+=1
        if i==7:
            print("You lose.")
            break
            
     else:
        for i in range(len(select)):
            item=select[i]
            if item==letters:
                word_shape[i]=item

            
     print(word_shape)
     if "_" not in word_shape:
        End_Of_Game=True
        print("You Win.")
