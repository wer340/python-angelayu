class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0


user_1 = User("001", "Scarlett")
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Scarlett"

user_2 = User("002", "Emilia")
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Emilia"

user_3 = User("003", "Jodi")
# user_3 = User()
# user_3.id = "003"
# user_3.username = "Jodi"

user_4 = User("004", "Audry")
# user_4 = User()
# user_4.id = "004"
# user_4.username = "Audry"

user_5 = User("005", "Margot")
# user_5 = User()
# user_5.id = "005"
# user_5.username = "Margot"

print(
    f"wolf of wall street:{user_5.username} , Game of thrones : {user_2.username}")
print(
    f"wolf of wall street:{user_5.followers} , Game of thrones : {user_3.followers}")
