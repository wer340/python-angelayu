def mutate(a_list):
    b_list=[]
    for item in a_list:
        new_item=item*2
        b_list.append(new_item) #pythontutor.com   this line not there in for -loop
    print(b_list)

mutate([1,2,3,5,8,13])