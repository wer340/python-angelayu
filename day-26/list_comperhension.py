list=["using","list","comprehension",2022]
name="scarlet"
sentence=' '.join([str(item) for item in list])
new_name=' '.join([letter+"❤" for letter in name])
print(sentence,new_name)

numbers=[num*2 for num in range(1,6)]
print(numbers)