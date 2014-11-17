__author__ = 'tivvit'


from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop

from protorpc import messages

from cdh_m import User_m
from cdh_m import UsersCollection_m

from cdh_m import SolvedQuestSum_m
from cdh_m import SolvedQuest_m
from cdh_m import SolvedQuestsCollection_m

from solved_quest import SolvedQuest

from quests import Quests

import logging


class Users(ndb.Model):
    # id = messages.IntegerField(1)
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    faction = ndb.IntegerProperty()

    # user = msgprop.MessageProperty(User_m, indexed_fields=['name', 'faction'])

    # def __init__(self):
    #     self.solved_quest = SolvedQuest()

    def list(self):
        users = []
        for user in Users.query().fetch():
            users.append(self._map_message(user))

        logging.info(users)
        return UsersCollection_m(user=users)

    def get(self, id):
        #todo query param
        return self._map_message(ndb.Key(Users, id).get())

    def delete(self, id):
        #todo query param
        return ndb.Key(Users, id).delete()

    def set_faction(self, user_id, faction_id):
        user = ndb.Key(Users, user_id).get()
        user.faction = faction_id
        user.put()

        #todo check limits
        return self._map_message(user)

    def create(self, name, email, faction=0):
        user = Users(
            name=name,
            email=email,
            faction=faction
        )

        user.put()
        return self._map_message("%", user)

    def get_points(self, user_id):
        solved_quest = SolvedQuest()
        solved = solved_quest.get_user_points_list(user_id)

        # logging.debug(solved)

        solved_quests = []
        for solve in solved:

            if solve.id_quest:
                quest = Quests().get(solve.id_quest)
            else:
                quest = None

            solved_quests.append(
                SolvedQuest_m(
                    userId = solve.id_user,
                    questId = solve.id_quest,
                    points = solve.points,
                    quest = quest
                )
            )

        return SolvedQuestsCollection_m(solved_quests=solved_quests)

    def get_points_sum(self, user_id):
        solved_quest = SolvedQuest()
        return solved_quest.get_user_points_sum(user_id)

    def get_points_sum_m(self, user_id):
        return SolvedQuestSum_m(
            sum=self.get_points_sum(user_id)
        )

    def add_points(self, user_id, points):
        solved_quest = SolvedQuest()
        points = solved_quest.add_points(user_id, points)

        return SolvedQuest_m(
            userId=points.id_user,
            points=points.points
        )

    def solve_quest(self, user_id, quest_id):
        solved_quest = SolvedQuest()

        quests = Quests()
        points = quests.get(quest_id).points

        solved = solved_quest.solve_quest(user_id, quest_id, points)

        logging.warning(solved)

        return SolvedQuest_m(
            userId=solved.id_user,
            questId=solved.id_quest,
            points=solved.points
        )

    def _map_message(self, user):
        return User_m(
            name=user.name,
            email=user.email,
            faction=user.faction,
            id=user.key.id()
        )
