__author__ = 'tivvit'

from protorpc import messages

class Stats_m(messages.Message):
    points = messages.IntegerField(1)

class FactionUsers_m(messages.Message):
    users = messages.IntegerField(1)

class FactionId_m(messages.Message):
    id = messages.IntegerField(1)

class FactionStats_m(messages.Message):
    #todo this has to be structures
    stats = messages.MessageField(Stats_m, 1, repeated=True)
    users = messages.MessageField(FactionUsers_m, 2, repeated=True)


