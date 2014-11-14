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
            if user.user.faction:
                users[user.user.faction] += 1

        faUsers = []
        for usr in users:
            faUsers.append(FactionUsers(users=usr))

        #todo user ponts
        stats = []
        for usr in points:
            stats.append(Stats(points=usr))

        logging.info("%s", users)

        return FactionStats(users=faUsers, stats=stats)

