__author__ = 'tivvit'

from protorpc import messages

class User_m(messages.Message):
    name = messages.StringField(1)
    email = messages.StringField(2)
    faction = messages.IntegerField(3)
    id = messages.IntegerField(4)
    # inserted = messages.DateTimeField(5)

class UsersCollection_m(messages.Message):
    user = messages.MessageField(User_m, 1, repeated=True)