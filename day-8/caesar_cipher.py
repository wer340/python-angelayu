from logo import logo
import os
os.system('cls')
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z'] 
# decode  and encode    shift  * -1  ✅🌿

def encrypt(plain_text,shift_value):
    encode_text=""
    for char in plain_text:
        index=letters.index(char)
        # print(f"index={index} \n")
        new_position=index+shift_value
        if new_position>25:
            new_position-=25
        encode_text+=letters[new_position]
    print(f"your encrypt text {encode_text}  ")

def decrypt(plain_text,shift_value):
    decode_text=""
    for char in plain_text:
            index=letters.index(char)
            # print(f"index={index} \n")
            new_position=index-shift_value
            if new_position<0:
                new_position+=25
            decode_text+=letters[new_position]
    print(f"your decrypt text {decode_text}  ")

def checker_shift(number):
    if number>26:
        return number%26
    else:
        return number

break_time=True
while break_time:
    os.system('cls')
    print(logo)
    direction=input("type 'encode' to encrypt , type 'decode' to decrypt \n")
    text=input("Type your message : \n").lower()
    shift=int(input("Type the shift number : \n"))
    shift=checker_shift(shift)
    if direction=="encode":
        encrypt(plain_text=text,shift_value=shift)
    else:
        decrypt(plain_text=text,shift_value=shift)
    exit=input("for exit Y ")
    if exit=="Y":
        break_time=False
        print("good bye")
        