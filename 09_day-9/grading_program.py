list_dictionary={
"Scarlett Johansson":84,
"Sharon Stone":58,
"Jennifer Connelly":70,
"Brooke Shields":65,
"Monica Bellucci":64,
"Emilia Clarke":85,
"Sarah Catherine Hook":95
}
grade={}
for key in list_dictionary:
    value_list=list_dictionary[key]
    if value_list>90 and value_list<100:
        grade[key]="Outstanding"
    elif value_list>80 and value_list<90:
        grade[key]="Exceeds Expection"
    elif value_list>71 and value_list<80:
        grade[key]="Acceptable"
    elif  value_list<70:
        grade[key]="Fail"

print(grade)