__author__ = 'tivvit'

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

import logging

from model import Users
from user_messages import User
from user_messages import UsersCollection

from model import Quests
from user_messages import Quest
from user_messages import QuestsCollection

from model import Game
from user_messages import FactionStats

package = 'Devfest_CDH'

@endpoints.api(name='devfest_cdh_api', version='v1', description='Devfest 2014 CDH API')
class DevfestCdhApi(remote.Service):

    def __init__(self):
        self.users = Users()
        self.quests = Quests()
        self.game = Game()

    """
        Users
    """
    @endpoints.method(message_types.VoidMessage, UsersCollection,
                      path='user', http_method='GET',
                      name='users.list')
    def users_list(self, unused_request):
        return self.users.list()

    ID_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            id=messages.IntegerField(1, variant=messages.Variant.INT32))

    @endpoints.method(ID_RESOURCE, User,
                      path='user/{id}', http_method='GET',
                      name='users.getUser')
    def user_get(self, request):
        try:
            return self.users.get(request.id)
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('User %s not found.' %
                                              (request.id))

    MULTIPLY_METHOD_RESOURCE = endpoints.ResourceContainer(
        User)
        # ,
        # name=messages.StringField(2, variant=messages.Variant.STRING,
        #                             required=True))

    @endpoints.method(MULTIPLY_METHOD_RESOURCE, User,
                      path='user', http_method='POST',
                      name='users.addUser')
    def user_add(self, request):
        return self.users.create(request.name, request.email, request.faction)
        #return User(name=request.name) #* request.name

    @endpoints.method(ID_RESOURCE, User,
                      path='user/{id}', http_method='DELETE',
                      name='users.delUser')
    def user_delete(self, request):
        try:
            return self.users.delete(request.id)
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('User %s not found.' %
                                              (request.id,))

    """
        Quests
    """
    @endpoints.method(message_types.VoidMessage, QuestsCollection,
                      path='quest', http_method='GET',
                      name='quests.list')
    def quests_list(self, unused_request):
        return self.quests.list()

    ID_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            id=messages.IntegerField(1, variant=messages.Variant.INT32))

    @endpoints.method(ID_RESOURCE, Quest,
                      path='quest/{id}', http_method='GET',
                      name='quests.getQuest')
    def quest_get(self, request):
        try:
            return self.quests.get(request.id)
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Quest %s not found.' %
                                              (request.id))

    MULTIPLY_METHOD_RESOURCE = endpoints.ResourceContainer(
        Quest)
        # ,
        # name=messages.StringField(2, variant=messages.Variant.STRING,
        #                             required=True))

    @endpoints.method(MULTIPLY_METHOD_RESOURCE, Quest,
                      path='quest', http_method='POST',
                      name='quests.addQuest')
    def quest_add(self, request):
        return self.quests.create(request.name, request.faction, request.points)
        #return User(name=request.name) #* request.name

    @endpoints.method(ID_RESOURCE, Quest,
                      path='quest/{id}', http_method='DELETE',
                      name='quests.delQuest')
    def quest_delete(self, request):
        try:
            return self.quests.delete(request.id)
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Quest %s not found.' %
                                              (request.id,))

    """
        Game
    """
    @endpoints.method(message_types.VoidMessage, FactionStats,
                      path='stats', http_method='GET',
                      name='faction.Stats')
    def faction_stats_get(self, request):
        try:
            return self.game.stats()
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Quest %s not found.')


APPLICATION = endpoints.api_server([DevfestCdhApi])