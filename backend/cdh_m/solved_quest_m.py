__author__ = 'tivvit'

from protorpc import messages

from quest_m import Quest_m

class SolvedQuestSum_m(messages.Message):
    sum = messages.IntegerField(1)

class SolvedQuest_m(messages.Message):
    userId = messages.IntegerField(1)
    questId = messages.IntegerField(2)
    points = messages.IntegerField(3)
    quest = messages.MessageField(Quest_m, 4)
    # inserted = messages.DateTimeField(5)

class SolvedQuestsCollection_m(messages.Message):
    solved_quests = messages.MessageField(SolvedQuest_m, 1, repeated=True)