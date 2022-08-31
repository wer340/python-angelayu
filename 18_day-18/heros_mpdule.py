import heroes
list=[]

for _ in range(50):
    list.append(heroes.gen())

print(list)