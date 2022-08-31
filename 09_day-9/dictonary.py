
#{"key":"value"}
list_dictionary={
"Scarlett Johansson":"Avengers: Endgame",
"Sharon Stone":"Basic Instinct",
"Jennifer Connelly":"A Beautiful Mind",
"Brooke Shields":"The Blue Lagoon",
"Monica Bellucci":"Malena"
}
print(list_dictionary["Monica Bellucci"])
list_dictionary["Angelina Jolie"]="Maleficent"
# print(list_dictionary)

#loop

for Actress  in list_dictionary:
    print(f"\n ********************\n {Actress} play in {list_dictionary[Actress]} movie\n")