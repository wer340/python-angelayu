import pandas
data=pandas.read_csv("./wheather_sheet.csv")
print(data)

#loop through row   use Dataframe.iterrows()
for (key,value) in data.iterrows():
    print(key)
    print(value.codition)