import pandas
with open("./wheather_sheet.csv") as wheather:
    data=pandas.read_csv(wheather)
    fa="dd"
    print(type(data) )
    print(type(data["temp"]) )
    print(data.to_dict())
    print(data["temp"].to_list())
