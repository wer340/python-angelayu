def add_sum(*numbers):  #deafult name *args
    # print(type(*numbers)) no type many arg astrix a sign
    print(type(numbers))  #tuple
    print(numbers[14])
   # tuple    this star a sign  for interpreter that args get and put in tuple collection
    return sum(numbers)

print(
    add_sum(3, 4, 6, 7, 8, 9, 4, 2, 1, 1, 4, 5, 6, 7, 88, 8, 8, 8, 8,
            8))
