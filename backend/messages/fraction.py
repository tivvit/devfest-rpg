__author__ = 'tivvit'

from google.appengine.ext import ndb


class Fraction(ndb.Model):
    id = ndb.IntegerProperty()
    name = ndb.StringProperty()
