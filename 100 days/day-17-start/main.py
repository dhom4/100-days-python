""" Notes
#1 a Constructor: part of the blueprint that allows us to specify what should happen when our object is being constructed.
#2 using special function:
    def __init__(self, ...):
    #initialise attributes
    this inside special function is where we create the starting values for out attributes.
    the init function is ganna be called every time you create a new object.

"""
# class declaration
class User:
    def __init__(self, user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# Building an object out of that class
user_1 = User(1,"abdi")
user_2 = User(2,"casha")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

