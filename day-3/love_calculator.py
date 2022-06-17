#print("how much love together !!!")
message="please put your name  a ? "
name_a=input(message)
message="please put your name  b ? "
name_b=input(message)
true=0
love=0
true+=(name_a+name_b).lower().count("t")
true+=(name_a+name_b).lower().count("r")
true+=(name_a+name_b).lower().count("u")
true+=(name_a+name_b).lower().count("e")
love+=(name_a+name_b).lower().count("l")
love+=(name_a+name_b).lower().count("o")
love+=(name_a+name_b).lower().count("v")
love+=(name_a+name_b).lower().count("e")
total_score_str=str(true)+str(love)
total=int(total_score_str)
if total>90 or total<10:
    message=f"your score is {total} you go together like coke and mentos "
    print(message)
elif total>40 and total<50 :
    message=f"your score is {total} you are alright together"
    print(message)
else:
    message=f"your score is {total}"
    print(message)