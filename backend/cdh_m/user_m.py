__author__ = 'tivvit'

from protorpc import messages

from quest_m import Quest_m
from solved_quest_m import SolvedQuest_m

class User_m(messages.Message):
    name = messages.StringField(1)
    email = messages.StringField(2)
    faction = messages.StringField(3)
    id = messages.IntegerField(4)
    factionId = messages.IntegerField(5)

class User_stats_m(messages.Message):
    user = messages.MessageField(User_m, 1)
    quests = messages.MessageField(SolvedQuest_m, 2, repeated=True)
    todo = messages.MessageField(Quest_m, 3, repeated=True)
    pointsSum = messages.IntegerField(4)
    allowedToFaction = messages.IntegerField(5)


class UsersCollection_m(messages.Message):
    user = messages.MessageField(User_m, 1, repeated=True)