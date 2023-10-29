"""class User:
    pass


user_1 = User()
user_1.name ='John'
user_1.email ='john@example.com'

print(user_1.name)"""


class User:
    def __init__(self,user_id, username):
        self.user_id = user_id
        self.username = username
        self.follower_count = 0


user_1 = User(1,'John')
user_2 = User(2,'Damu')
user_1.username = 'Rajini'

print(user_1.username,user_2.follower_count)
        


