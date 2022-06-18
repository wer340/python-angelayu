row1=["⬜","⬜","⬜"]
row2=["⬜","⬜","⬜"]
row3=["⬜","⬜","⬜"]
row=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
number=input("please type number ?  ")
row_number=int(number[0])
column_number=int(number[1])
print (f"row = {row_number} and column = {column_number}")
row[row_number][column_number]="X"
print(f"{row1}\n{row2}\n{row3}")