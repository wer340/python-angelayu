import pandas
with open("./wheather_sheet.csv") as wheather:
    data = pandas.read_csv(wheather)
    # get a row data  a little hard
    row_24 = data[data.temp == 24]
    print(f"record of temp=24:\n********************\n {row_24}")
    temp_f = row_24.temp * (9 / 5) + 32
    print(type(temp_f))
    print(temp_f)
