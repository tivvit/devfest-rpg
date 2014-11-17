__author__ = 'tivvit'

from model import Users
from cdh_m import User_m
from cdh_m import UsersCollection_m

from cdh_m import FactionStats_m
from cdh_m import Stats_m
from cdh_m import FactionUsers_m

import logging

class Game(object):

    def __init__(self):
        self.users = Users()

    def stats(self):
        users = [0, 0, 0]
        points = [0, 0, 0]

        logging.info("%s", users)

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

