__author__ = 'tivvit'

from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop

from protorpc import messages

from backend.cdh_m import User_m, UsersCollection_m, SolvedQuestSum_m, SolvedQuest_m, SolvedQuestsCollection_m
from solved_quest import SolvedQuest
from quests import Quests

from faction_names import faction_names
# from game import Game

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
        for user in Users.query().order(Users.name).fetch():
            users.append(self._map_message(user))

        # logging.info(users)
        return UsersCollection_m(user=users)

    def search(self, query):
        users = []
        # for user in Users.query(Users.name==query).fetch():
        # todo use search API
        for user in Users.query().fetch():
            if user.name and query in user.name:
                users.append(self._map_message(user))

        logging.info(users)
        return UsersCollection_m(user=users)

    def get(self, id):
        return self._map_message(ndb.Key(Users, id).get())

    def delete(self, id):
        return ndb.Key(Users, id).delete()

    def allowed_to_faction(self, game, user_id):
        user_points = self.get_points_sum(user_id)
        print "points" + str(user_points)
        print game.get_min_faction_points()
        return user_points >= game.get_min_faction_points()

    def set_faction(self, game, user_id, faction_id):
        user = ndb.Key(Users, user_id).get()

        print self.allowed_to_faction(game, user_id)
        print game.faction_hiring(faction_id).hiring
        if not user.faction and self.allowed_to_faction(game, user_id) and game.faction_hiring(faction_id).hiring:
            user.faction = faction_id
            user.put()

        return self._map_message(user)

    def create(self, name, email, faction=0):
        user = Users(
            name=name,
            email=email,
            faction=faction
        )

        user.put()
        return self._map_message(user)

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
                    userId=solve.id_user,
                    questId=solve.id_quest,
                    points=solve.points,
                    quest=quest
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
        # solved_quest = SolvedQuest()

        # quests = Quests()
        quest = Quests.query(Quests.num == quest_id).get()
        points = quest.points

        user = ndb.Key(Users, user_id).get()

        logging.info(user.faction)
        logging.info(quest.faction)

        if quest.faction == 0 or quest.faction == user.faction:
            solved_c = self.get_points(user_id)
            solved_c = solved_c.solved_quests

            alreadySolved = False

            for s in solved_c:
                if s.quest and quest.num == s.quest.num:
                    alreadySolved = True
                    break

            if not alreadySolved:
                solved_quest = SolvedQuest()
                solved = solved_quest.solve_quest(user_id, quest_id, points)
                logging.warning(solved)

                return SolvedQuest_m(
                    userId=solved.id_user,
                    questId=solved.id_quest,
                    points=solved.points
                )
            # else:
            #     raise Exception
        else:
            raise Exception

    def get_stats(self, game, user_id, faction_id):
        from backend.cdh_m import Quest_m, User_stats_m

        user = ndb.Key(Users, user_id).get()
        user_m = self._map_message(user)
        # q = []
        # q.append(Quest_m(name="Zabij vsechny kolem", faction="Nefrakcni", points=2))
        # q.append(Quest_m(name="Zabij vsechny Vitalisty", faction="Metalide", points=10))

        #logging.debug()

        solved = self.get_points(user_id)
        solved = solved.solved_quests

        # solved = []
        # for s in solved_c:
        #     if s.quest:
        #         solved.append(s.quest)

        q = Quests()
        list_faction = 0
        if user.faction == faction_id:
            list_faction = faction_id

        todo = q.list_by_fraction(list_faction)
        todo = todo.quest

        # logging.info("cnt: " + todo)
        # logging.info(">>>>>>>>>>>>>>")

        filtered_todo = []

        for t in todo:
            add = True
            # logging.info(solved)
            # logging.info("========")
            logging.info("========")
            for solv in solved:
                # logging.info("solv" + solv.num)
                # logging.info("todo" + t.num)

                if t.num and solv.quest and solv.quest.num == t.num:
                    add = False
                    break

            if add:
                filtered_todo.append(t)

        return User_stats_m(
            user=user_m,
            todo=filtered_todo,
            quests=solved,
            pointsSum=self.get_points_sum(user_id),
            allowedToFaction=int(user.faction == 0 and self.allowed_to_faction(game, user_id) and game.faction_hiring(faction_id))
        )

    def _map_message(self, user):
        return User_m(
            name=user.name,
            email=user.email,
            factionId=user.faction,
            faction=faction_names[user.faction] if user.faction else "",
            id=long(user.key.id())
        )
