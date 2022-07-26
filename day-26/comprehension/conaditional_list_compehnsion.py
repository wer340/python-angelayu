import re
names=["1_Scarlett_Johansson",
    "2_Jennifer_Lawrence",
    "3_Emma_Watson",
    "4_Anne_Hathaway",
    "5_Natalie_Portman",
    "6_Emma_Stone",
    "7_Gal_Gadot",
    "8_Alexandra_Daddario",
    "9_Margot_Robbie",
    "10_Megan_Fox",
    "11_Emily_Blunt",]
regex="\d{1,3}_|_" # | or digit or underscore
new_list=[name.replace(regex,"") for name in names if len(name)<15]
new_list2=[re.sub(regex," ",name).strip() for name in names if len(name)<15]
new_list3=[ re.sub("\A|\Z","❤",name) for name in new_list2 ]
print(new_list2)