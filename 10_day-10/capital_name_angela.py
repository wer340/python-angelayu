
#title case
#.title()
def format_name(f_name,l_name):
    f_name=f_name.title()
    l_name=l_name.title()
    return[f_name,l_name]

result=format_name("scarlett","johansson")
print(f" name is {result[0]} and last name is {result[1]} ")
