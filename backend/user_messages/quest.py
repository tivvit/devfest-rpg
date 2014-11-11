__author__ = 'tivvit'

from protorpc import messages

class Quest(messages.Message):
    name = messages.StringField(1)
    fraction = messages.IntegerField(2)
    points = messages.IntegerField(3)
    # inserted = messages.DateTimeField(5)

class QuestsCollection(messages.Message):
    quest = messages.MessageField(Quest, 1, repeated=True)