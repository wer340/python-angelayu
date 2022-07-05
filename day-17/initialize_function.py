i=1
class User:
    i=1

    def __init__(self):
        global i
        print(
            f"you just every time run time:{i}")  # every time object create init functon run
        i +=1

user_1 = User()
user_1.id = "001"
user_1.username = "Scarlett"

user_2 = User()
user_2.id = "002"
user_2.username = "Emilia"

user_3 = User()
user_3.id = "003"
user_3.username = "Jodi"
