list_dictionary=[
{"Scarlett Johansson":{
    "movies":["Avengers: Endgame","Lost in Translation","Her","The Avengers","Ghost World"],"age":38}
},
{"Sharon Stone":["Basic Instinct","Casino,The Quick and the Dead","Sliver"]},
{"Jennifer Connelly":["A Beautiful Mind","House of Sand and Fog","Requiem for a Dream","The Rocketeer"]},
{"Brooke Shields":["The Blue Lagoon","Pretty Baby","Wanda Nevada","The Midnight Meat Train"]},
{"Monica Bellucci":["Malena","The Matrix Revolutions","The Matrix Reloaded","Shoot 'Em Up"]}
]
print(list_dictionary[0]["Scarlett Johansson"]["movies"][4])
print(list_dictionary[1]["Sharon Stone"][2])

list_dictionary.append({"Audrey Hepburn":["Breakfast at Tiffany's","Roman Holiday","Charade","My Fair Lady"]})
print(list_dictionary[5])