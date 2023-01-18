class user:
    def __init__(self, userid, username):
        self.id = userid
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user1 = user("001", "Sukumar")
user2 = user("002", "Sushree")
user1.follow(user2)
print(user1.follower)
print(user1.following)
print(user2.follower)
print(user2.following)