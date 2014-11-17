__author__ = 'tivvit'


from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop

from protorpc import messages

from cdh_m import Quest_m
from cdh_m import QuestsCollection_m

import logging


class Quests(ndb.Model):
    name = ndb.StringProperty()
    faction = ndb.IntegerProperty()
    points = ndb.IntegerProperty()

    #quest = msgprop.MessageProperty(Quest_m, indexed_fields=['name', 'faction'])

    def list(self):
        quests = []
        for quest in Quests.query().fetch():
            quests.append(self._mapMessage(quest))

        logging.info(quests)
        return QuestsCollection_m(quest=quests)

    def list_by_fraction(self, id_fraction):
        quests = []
        for quest in Quests.query(Quests.faction == id_fraction).fetch():
            quests.append(self._mapMessage(quest))

        logging.info(quests)
        return QuestsCollection_m(quest=quests)

    def get(self, id):
        return self._mapMessage(ndb.Key(Quests, id).get())

    def delete(self, id):
        return ndb.Key(Quests, id).delete()

    def create(self, name, faction, points):
        quest = Quests(
            name=name,
            faction=faction,
            points=points
        )

        quest.put()
        return self._mapMessage(quest)

    def _mapMessage(self, quest):
        return Quest_m(
            name=quest.name,
            faction=quest.faction,
            points=quest.points,
            id=quest.key.id()
        )

