print("average height of student")
#you cant use  sum()  and len() function
heights=input("type list of height of student ? ").split()
sum_height=0
cunter=0
for height in heights:
    sum_height+=int(height)
    cunter+=1

average=sum_height/cunter

print(f"average of student is = {average}")