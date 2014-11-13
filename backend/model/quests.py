__author__ = 'tivvit'


from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop

from protorpc import messages

from user_messages import Quest
from user_messages import QuestsCollection

import logging


class Quests(ndb.Model):
    quest = msgprop.MessageProperty(Quest, indexed_fields=['name', 'faction'])

    def list(self):
        #todo list by fraction?
        quests = []
        for quest in Quests.query().fetch():
            quests.append(quest.quest)

        logging.info(quests)
        return QuestsCollection(quest=quests)

    def get(self, id):
        #todo query param
        return ndb.Key(Quest, id).get().quest

    def delete(self, id):
        #todo query param
        return ndb.Key(Quest, id).delete

    def create(self, name, faction, points):
        quest = Quest(
            name=name,
            faction=faction,
            points=points
        )

        Quests(quest=quest).put()
        return quest

