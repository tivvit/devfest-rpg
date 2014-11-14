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

import logging


class Users(ndb.Model):
    user = msgprop.MessageProperty(User_m, indexed_fields=['name', 'faction'])

    def __init__(self):
        self.solved_quest = SolvedQuest()

    def list(self):
        users = []
        for usr in Users.query().fetch():
            users.append(usr.user)

        logging.info(users)
        return UsersCollection_m(user=users)

    def get(self, id):
        #todo query param
        return ndb.Key(Users, id).get().user

    def delete(self, id):
        #todo query param
        return ndb.Key(Users, id).delete()

    def set_faction(self, user_id, faction_id):
        user = Users.query(Users.id == user_id).get()
        user.faction = faction_id
        user.put()

    def create(self, name, email, faction = None):
        user = User_m(
            name=name,
            email=email,
            faction=faction
        )

        Users(user=user).put()

        return user

    def get_points(self, user_id):
        self.solved_quest.get_user_points_list(user_id)

    def get_points_sum(self, user_id):
        return SolvedQuestSum_m(
            sum=self.solved_quest.get_user_points_sum(user_id)
        )

    def add_points(self, user_id, quest_id):
        points = self.solved_quest.add_points(user_id, quest_id)

        return SolvedQuest_m(
            # userId=points.user_id,
            # points=points.points
        )

    def solve_quest(self, user_id, quest_id):
        solved = self.solved_quest.solve_quest(user_id, quest_id, 10)

        logging.warning("xxxxx")
        logging.warning(solved)

        # todo find quest

        return SolvedQuest_m(
            # sints
        )


