
#flower  my_function car brand     all of thing that called with name is a namespace

flower="rose" #global scope


def my_function(name):
    car="benz"#local scope
    flower="blue rose"
    print(flower) #output 2
    print(name)  #output 3

#print(car)#not print  beceause car in local scop

if 3>2:
    brand="apple" #global scope       #c++ java block of code have scope   but python havent this property
    print(flower) #output 1

my_function(brand)