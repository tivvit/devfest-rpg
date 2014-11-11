__author__ = 'tivvit'

from protorpc import messages
from google.appengine.ext.ndb import msgprop

class User(messages.Message):
    id = messages.IntegerField(1)
    name = messages.StringField(2)
    mail = messages.StringField(3)
    fraction = messages.IntegerField(4)
    # inserted = messages.DateTimeField(5)

class UsersCollection(messages.Message):
    user = messages.MessageField(User, 1, repeated=True)