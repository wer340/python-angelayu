import pandas_effort
import math
with open("./wheather_sheet.csv") as wheather:
    data = pandas.read_csv(wheather)
    fa = "dd"
    print(type(data))
    print(type(data["temp"]))
    print(data.to_dict())
    print(data["temp"].to_list())
    average_temp = 0
    for temp in data["temp"]:
        average_temp += temp

    average_temp /= len(data["temp"])

    print(f"average temperature : {math.ceil(average_temp)}")
    #another way
    average_temp2=sum(data["temp"])/len(data["temp"])
    print(f"average temerature : {average_temp2}")
    #pandas way☕
    pd_aaverage=data["temp"].mean()
    # print(f"average pandas way : {pd_aaverage}")
    # print(data["temp"].max())
