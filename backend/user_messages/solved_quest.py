__author__ = 'tivvit'

from protorpc import messages

class SolvedQuest(messages.Message):
    userId = messages.IntegerField(1)
    questId = messages.IntegerField(2)
    points = messages.IntegerField(3)
    # inserted = messages.DateTimeField(5)

class SolvedQuestsCollection(messages.Message):
    solved_quests = messages.MessageField(SolvedQuest, 1, repeated=True)