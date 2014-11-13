__author__ = 'tivvit'

from protorpc import messages

class Stats(messages.Message):
    points = messages.IntegerField(1)

class FactionUsers(messages.Message):
    users = messages.IntegerField(1)

class FactionStats(messages.Message):
    #todo this has to be structures
    stats = messages.MessageField(Stats, 1, repeated=True)
    users = messages.MessageField(FactionUsers, 2, repeated=True)


