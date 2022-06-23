import random
import hangman_shape
word_list=["ardvark" , "baboon" ,"camel"]

select=random.choice(word_list)
print(select)
word_shape=[]

for _ in select:
    word_shape+="_"
End_Of_Game=False
lives=7
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
    elif letters not in select:
        print(hangman_shape.hangman_pics[7-lives])
        lives-=1
        if lives==0:
                print("You Lose")
                End_Of_Game=True


#instead of break   use  end_of_game   and false condition while loop   all thing into if before pop of loop