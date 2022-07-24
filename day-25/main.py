import csv
with open("./wheather_sheet.csv") as wheather:
    data=csv.reader(wheather) #create object
    for row in data:
        print(row)