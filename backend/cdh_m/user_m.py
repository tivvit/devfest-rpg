__author__ = 'tivvit'

from protorpc import messages

class User_m(messages.Message):
    id = messages.IntegerField(1)
    name = messages.StringField(2)
    email = messages.StringField(3)
    faction = messages.IntegerField(4)
    # inserted = messages.DateTimeField(5)

class UsersCollection_m(messages.Message):
    user = messages.MessageField(User_m, 1, repeated=True)