__author__ = 'tivvit'


from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop

from protorpc import messages

from messages import User
from messages import UsersCollection

import logging


class Users(ndb.Model):
    user = msgprop.MessageProperty(User, indexed_fields=['id', 'name', 'fraction'])

    def list(self):
        users = []
        for usr in Users.query().fetch():
            users.append(usr.user)

        logging.info(users)
        return UsersCollection(user=users)

    def get(self, id):
        #todo query param
        return ndb.Key(Users, id).get().user

    def set_fraction(self, user_id, fraction_id):
        user = Users.query(Users.id == user_id).get()
        user.fraction = fraction_id
        user.put()

    # def create(self, name, email):
    def create(self):
        user = User(
            name='tivvit'
        )

        Users(user=user).put()

        # if not Users.query().count():
        #     users = Users(users=UsersCollection(user=user))
        #     users.put()
        #
        # u = Users.query().get().users.user
        # u.append(user)
        # # users = Users(users=UsersCollection(user=user))
        # key = u.put()

