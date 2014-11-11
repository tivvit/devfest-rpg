__author__ = 'tivvit'

from google.appengine.ext import ndb


class Quest(ndb.Model):
    id = ndb.IntegerProperty()
    points = ndb.StringProperty()
    fraction = ndb.IntegerProperty('r')
    inserted = ndb.DateTimeProperty(auto_now_add=True)
