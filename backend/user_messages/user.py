__author__ = 'tivvit'

from protorpc import messages

class User(messages.Message):
    name = messages.StringField(1)
    email = messages.StringField(2)
    faction = messages.IntegerField(3)
    # inserted = messages.DateTimeField(5)

class UsersCollection(messages.Message):
    user = messages.MessageField(User, 1, repeated=True)