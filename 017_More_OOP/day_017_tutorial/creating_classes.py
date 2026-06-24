class User: # Should use pascal case for naming each class.


    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("New user created")


    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("001", "SalmanSaeed")
user2 = User("002", "JackSparrow")

print(user1.user_id)

user1.follow(user2)

print(user2.followers)
print(user1.following)