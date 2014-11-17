__author__ = 'tivvit'

from users import Users

from backend.cdh_m import  User_m, UsersCollection_m, FactionStats_m, Stats_m, FactionUsers_m, Leaderboard_entry_m, Leaderboard_m

import logging

class Game(object):

    def __init__(self):
        self.users = Users()

    def stats(self):
        users = [0, 0, 0]
        points = [0, 0, 0]

        logging.info("%s", users)

        leaderboard = []

        for user in Users.query().fetch():
            if user.faction:
                users[user.faction] += 1
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
        leaderboard = []

        for user in Users.query().fetch():
            leaderboard.append(Leaderboard_entry_m(
                user=user.get(user.key.id()),
                points=user.get_points_sum(user.key.id())
            ))

        leaderboard.sort(key=lambda x: x.points, reverse=True)

        return Leaderboard_m(leaderboard=leaderboard[:limit])

