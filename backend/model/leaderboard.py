__author__ = 'tivvit'


from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop
from protorpc import messages

from backend.cdh_m import Leaderboard_m

class Leaderboard(ndb.Model):
    leaderboard = msgprop.MessageProperty(Leaderboard_m)