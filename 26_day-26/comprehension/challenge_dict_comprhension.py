sentance = "Scarlett Johansson is an American film actress and singer" \
           " who primarily works in Hollywood films. She was born on November 22," \
           " 1984, in New York City, New York, United States."

dict_sent = {sentance: len(sentance) for sentance in sentance.split()}
print(dict_sent)

sum_len = [dict_sent[item] for item in dict_sent]
print(sum(sum_len))
print(sum_len)
print(len(sum_len))
wheather={
    "Mon":23,
    "Tue":21,
    "Wed":27,
    "Thur":29,
    "Fri":25,
    "Sat":35,
    "Sun":39
}
farenheight_w={day:(value*9/5+32) for (day,value) in wheather.items()}
print(farenheight_w)