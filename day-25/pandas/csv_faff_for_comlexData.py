import csv
with open("./wheather_sheet.csv") as wheather:
    data=csv.reader(wheather) #create object
    temperture=[]
    for row in data:
        if row[1]!="temp":
            temperture.append(int(row[1]))

    print(temperture)
