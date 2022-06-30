for number in range(1,101):
    if number%3==0 or number%5==0:
        print("Fizz Buzz")
    if number%3==0:
        print("fizz")
    if number%5==0:
        print("buzz")
    else:
        print([number])