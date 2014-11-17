__author__ = 'tivvit'

from protorpc import messages

from user_m import User_m

class Stats_m(messages.Message):
    points = messages.IntegerField(1)

class FactionUsers_m(messages.Message):
    users = messages.IntegerField(1)

class FactionId_m(messages.Message):
    id = messages.IntegerField(1)

class Leaderboard_m(messages.Message):
    user = messages.MessageField(User_m, 1)
    points = messages.IntegerField(2)

class FactionStats_m(messages.Message):
    stats = messages.MessageField(Stats_m, 1, repeated=True)
    users = messages.MessageField(FactionUsers_m, 2, repeated=True)
    leaderboard = messages.MessageField(Leaderboard_m, 3, repeated=True)


