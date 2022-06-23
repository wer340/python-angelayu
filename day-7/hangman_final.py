import random
import hangman_shape
import list_words
import hangman_logo
import game_over_logo
select=random.choice(list_words.word_list).lower()
print(select)
word_shape=[]

for _ in select:
    word_shape+="_"
End_Of_Game=False
lives=7
print(hangman_logo.logo_hangman)
while not End_Of_Game:
    letters=input("\n\nplease enter your letter? ").lower()

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
                print(f"\n\nYou lose \n\n{game_over_logo.logo_lose}")
                End_Of_Game=True
        else:
            print("\nyou lose a live !")
    else:
        print(f"\n{word_shape}")

#instead of break   use  end_of_game   and false condition while loop   all thing into if before pop of loop