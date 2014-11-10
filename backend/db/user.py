__author__ = 'tivvit'

# from google.appengine.ext import ndb

from protorpc import messages

class User(ndb.Model):
    id = ndb.IntegerProperty()
    name = ndb.StringProperty()
    mail = ndb.StringProperty()
    fraction = ndb.IntegerProperty('r')
    inserted = ndb.DateTimeProperty(auto_now_add=True)

    def get(self):
        return 0

    def create(self):
        user = User(
            name="test"
        )
        user.put()

