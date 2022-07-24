import pandas
with open("./wheather_sheet.csv") as wheather:
    data=pandas.read_csv(wheather)

    print(data["temp"])