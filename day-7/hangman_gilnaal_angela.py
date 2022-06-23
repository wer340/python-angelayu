import random
import hangman_shape
import list_words
import os
from hangman_logo import logo_hangman,logo_lose
select=random.choice(list_words.word_list).lower()
print(select)
word_shape=[]

for _ in select:
    word_shape+="_"
End_Of_Game=False
lives=7
print(logo_hangman)
while not End_Of_Game:
    letters=input("\n\nplease enter your letter? ").lower()
    os.system('cls')
    for num in range(len(select)):
        item=select[num]
        if item==letters:
            word_shape[num]=item
        
    
    if "_" not in word_shape:
        End_Of_Game=True
        print("\nYou Win.")
    elif letters not in select:
        print(hangman_shape.hangman_pics[7-lives])
        
        lives-=1
        if lives==0:
                print(f" \n\n{logo_lose}\n\nYou lose\n\n")
                End_Of_Game=True
        else:
            print(f"\n you type {letters} lose a live !")
    else:
        print(f"you type {letters} that s correct\n\n\n{word_shape}")

#instead of break   use  end_of_game   and false condition while loop   all thing into if before pop of loop
#use clear() func from replt lib   cleaar screen every time guess