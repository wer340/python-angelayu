print("welcome to the tip calculator !")
message="what was the total bill ? "
total_bill=float(input(message))#bill
message="what percentage tip would you like to give ? 10,12, or 15 ? "
my_mount_bill=int(input(message))*(total_bill/100)#tip
message="how many people to split the bill ?  "
number_person_bill=int(input(message))#people

result=(my_mount_bill+total_bill)/number_person_bill
result=round(result,2)#bill_with_tip
message=f"each person should pay : $ {result} "
print(message)