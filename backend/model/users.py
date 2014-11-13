__author__ = 'tivvit'


from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop

from protorpc import messages

from user_messages import User
from user_messages import UsersCollection

import logging


class Users(ndb.Model):
    user = msgprop.MessageProperty(User, indexed_fields=['name', 'faction'])

    def list(self):
        users = []
        for usr in Users.query().fetch():
            users.append(usr.user)

        logging.info(users)
        return UsersCollection(user=users)

    def get(self, id):
        #todo query param
        return ndb.Key(Users, id).get().user

    def delete(self, id):
        #todo query param
        return ndb.Key(Users, id).delete

    def set_faction(self, user_id, faction_id):
        user = Users.query(Users.id == user_id).get()
        user.faction = faction_id
        user.put()

    def create(self, name, email, faction = None):
        user = User(
            name=name,
            email=email,
            faction=faction
        )

        Users(user=user).put()

        return user

