__author__ = 'tivvit'

from model import Users
from user_messages import User
from user_messages import UsersCollection

from user_messages import FactionStats
from user_messages import Stats
from user_messages import FactionUsers

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

