def format_name(f_name,l_name):
    if f_name=="" or l_name=="" :
        return "You didnt provide valid inputs"#skip
    f_name=f_name.title()
    l_name=l_name.title()
    return f" name is {f_name} and last name is {l_name} "  #end of function

print(format_name("emilia","clarke"))
print(format_name("",""))