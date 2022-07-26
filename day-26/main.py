
import pandas
data=pandas.read_csv("./nato_phonetic_alphabet.csv")
#Loop through rows of a data frame
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()} convert tuple like items()

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#not use   to_dict method pandas
dict_nato={value.letter:value.code for (key,value) in data.iterrows()}
print(dict_nato)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

ask=input("please type your name?   : ").upper()
NATO_code=[dict_nato[char] for char in ask  ]
print(NATO_code)