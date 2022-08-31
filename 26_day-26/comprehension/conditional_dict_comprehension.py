from random import randint, seed

students = ['Scarlett Johansson', 'Jennifer Lawrence', 'Emma Watson',
            'Anne Hathaway', 'Natalie Portman', 'Emma Stone',
            'Gal Gadot', 'Alexandra Daddario', 'Margot Robbie',
            'Megan Fox', 'Emily Blunt']

seed(2022)  # be static score
dict_students = {student: randint(1, 100) for student in students}

print( dict_students.items())


# is select student that  get score  greater  than 60
#notice convert tuple type so dict also convert to tuple
dict_best_students={student:score for (student,score) in dict_students.items() if score>70 or student=='Scarlett Johansson' }

print(dict_best_students)
