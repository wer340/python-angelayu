class User:
    def __init__(self):
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


scarlett = User()
margot = User()
audry = User()
jenifer = User()
jenifer.follow(scarlett)
jenifer.follow(margot)
jenifer.follow(audry)
audry.follow(margot)
scarlett.follow(margot)
margot.follow(jenifer)
print(
    f"scarlett follower:{scarlett.follower} and  scarlett following:{scarlett.following}")
print(
    f"margot follower:{margot.follower} and  margot following:{margot.following}")
