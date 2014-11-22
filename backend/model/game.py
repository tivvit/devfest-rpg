__author__ = 'tivvit'

from users import Users
from leaderboard import Leaderboard
from backend.cdh_m import  User_m, UsersCollection_m, FactionStats_m, Stats_m, FactionUsers_m, Leaderboard_entry_m, Leaderboard_m, FactionFull_m, FactionMinPoints_m

import logging

from google.appengine.ext import ndb


class Game(ndb.Model):
    min_points = ndb.IntegerProperty()


    def stats(self):
        self.users = Users()
        users = [0, 0, 0]
        points = [0, 0, 0]

        for user in Users.query().fetch():
            if user.faction:
                users[user.faction-1] += 1
                points[user.faction-1] += user.get_points_sum(user.key.id())

        faUsers = []
        for usr in users:
            faUsers.append(FactionUsers_m(users=usr))

        stats = []
        for usr in points:
            stats.append(Stats_m(points=usr))

        logging.info("%s", users)

        return FactionStats_m(users=faUsers, stats=stats)

    def leaderboard(self, limit):

        lb_m = Leaderboard().query().get()
        return Leaderboard_m(leaderboard=lb_m.leaderboard[:limit])

        # leaderboard = []
        #
        # for user in Users.query().fetch():
        #     leaderboard.append(Leaderboard_entry_m(
        #         user=user.get(user.key.id()),
        #         points=user.get_points_sum(user.key.id())
        #     ))
        #
        # leaderboard.sort(key=lambda x: x.points, reverse=True)

        # return Leaderboard_m(leaderboard=leaderboard[:limit])

    def generateLeaderboard(self):
        leaderboard = []

        for user in Users.query().fetch():
            leaderboard.append(Leaderboard_entry_m(
                user=user.get(user.key.id()),
                points=user.get_points_sum(user.key.id())
            ))

        leaderboard.sort(key=lambda x: x.points, reverse=True)
        lb_m = Leaderboard_m(leaderboard=leaderboard)

        if Leaderboard().query().get():
            lb = Leaderboard().query().get()
            lb.leaderboard = lb_m
            lb.put()
        else:
            lb = Leaderboard(leaderboard=lb_m)
            lb.put()



    def leaderboard(self, limit):
        leaderboard = []

        for user in Users.query().fetch():
            leaderboard.append(Leaderboard_entry_m(
                user=user.get(user.key.id()),
                points=user.get_points_sum(user.key.id())
            ))

        leaderboard.sort(key=lambda x: x.points, reverse=True)

        return Leaderboard_m(leaderboard=leaderboard[:limit])

    def faction_hiring(self, faction_id):
        limit = 10
        game = Game()
        stats = game.stats()
        # stats = stats["stats"]

        print stats

        faction_min = stats.users[0].users
        faction_max = 0
        # faction_max = stats["users"][0]["users"]

        for users in stats.users:
            if faction_max < users.users:
                faction_max = users.users
            if faction_min > users.users:
                faction_min = users.users

        # print faction_max
        # print faction_min

        #print "M" + str(faction_max) + "N" + str(faction_min) + "ID " + str(faction_id) + str(stats.users[faction_id].users)
        return FactionFull_m(hiring=int(not (faction_max > (faction_min + limit) and stats.users[faction_id-1].users == faction_max)))

    def get_min_faction_points(self):
        game = Game.query().get()
        return game.min_points

    def get_min_faction_points_m(self):
        return FactionMinPoints_m(min=self.get_min_faction_points())

    def set_min_faction_points(self, new_min):
        min_points = Game.query().get()

        if not min_points:
            set_min_points = Game(min_points=new_min)
            set_min_points.put()

        min_points = Game.query().get()
        min_points.min_points = new_min
        min_points.put()

        return FactionMinPoints_m(min=min_points.min_points)


