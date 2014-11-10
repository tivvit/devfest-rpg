__author__ = 'tivvit'

from google.appengine.ext import ndb


class SolvedQuest(ndb.Model):
    id = ndb.IntegerProperty()
    name = ndb.StringProperty()
    userId = ndb.IntegerProperty('r')
    questId = ndb.IntegerProperty('r')
    points = ndb.IntegerProperty('r')
    inserted = ndb.DateTimeProperty(auto_now_add=True)
