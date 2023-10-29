class User:
    def __init__(self, user_id, username):
        self.username = username
        self.user_id = user_id
        self.follower_count = 0
        self.following_count = 0
    
    def follow(self,user):
        self.following_count += 1
        user.follower_count += 1
        
        
user_1 = User(1,'John')
user_2 = User(2,'Damu')

user_1.follow(user_2)
print(user_1.follower_count,user_1.following_count,user_2.follower_count,user_2.following_count)
#0110