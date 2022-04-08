#Class is just a blueprint for creating an object
#Class name = PascalCase

class User:
    score = 0
    def __init__(self, name: str, id: int, followers=0):
        print(f"New user is being created...")
        assert id >= 0, f"The id value must be greater than, or equal to 0."
        self.name = name
        self.id = id
        self.followers = followers

    def follow(self, user):
        self.followers += 1

    def function(self):
        pass


user_1 = User(name=input("Please enter your name: "), id=0o01)
user_2 = User(name=input("Please enter your name: "), id=0o01)
print(f"User Name: {user_1.name}")
print(f"User ID: {user_1.id}")
print(user_1.followers)

user_1.follow(user_2)
print(user_1.followers)

#Attribute is a variable associated with a project
# Attribute is a thing the object HAS i.e. followers
# Methods are a thing the object does i.e. def function() | essentially a function attached to an object
