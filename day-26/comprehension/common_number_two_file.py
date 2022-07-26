with open("./day-26-3-exercise/file1.txt") as file1:
    number_f1=[int(item) for item in file1.readlines()]
with open("./day-26-3-exercise/file2.txt") as file2:
    number_f2 = [int(item) for item in file2.readlines()]
    print(len(number_f1),len(number_f2))

new_list=[item for item in number_f1 if item in number_f2]
print(new_list)