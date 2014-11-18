__author__ = 'tivvit'

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

import logging

from model import Users
from cdh_m import User_m
from cdh_m import UsersCollection_m

from model import Quests
from cdh_m import Quest_m
from cdh_m import QuestsCollection_m

from model import Game
from cdh_m import FactionStats_m
from cdh_m import FactionId_m

from cdh_m import SolvedQuest_m
from cdh_m import SolvedQuestSum_m
from cdh_m import SolvedQuestsCollection_m

from cdh_m import Leaderboard_m

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
    @endpoints.method(message_types.VoidMessage, UsersCollection_m,
                      path='user', http_method='GET',
                      name='users.list')
    def users_list(self, unused_request):
        return self.users.list()

    QUERY = endpoints.ResourceContainer(
            message_types.VoidMessage,
            query=messages.StringField(1, variant=messages.Variant.STRING))

    @endpoints.method(QUERY, UsersCollection_m,
                      path='userSearch/{query}', http_method='GET',
                      name='users.search')
    def users_search(self, request):
        try:
            return self.users.search(request.query)
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('User %s not found.' %
                                              (request.id))

    ID_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            id=messages.IntegerField(1, variant=messages.Variant.INT64))


    @endpoints.method(ID_RESOURCE, User_m,
                      path='user/{id}', http_method='GET',
                      name='users.getUser')
    def user_get(self, request):
        try:
            return self.users.search(request.id)
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('User %s not found.' %
                                              (request.id))

    MULTIPLY_METHOD_RESOURCE = endpoints.ResourceContainer(User_m)
        # ,
        # name=messages.StringField(2, variant=messages.Variant.STRING,
        #                             required=True))

    @endpoints.method(MULTIPLY_METHOD_RESOURCE, User_m,
                      path='user', http_method='POST',
                      name='users.addUser')
    def user_add(self, request):
        return self.users.create(request.name, request.email) #, request.faction)
        #return User(name=request.name) #* request.name

    MULTIPLY_METHOD_RESOURCE_FACTION = endpoints.ResourceContainer(
        user_id=messages.IntegerField(2, variant=messages.Variant.INT64, required=True),
        faction_id=messages.IntegerField(3, variant=messages.Variant.INT64, required=True)
    )

    @endpoints.method(MULTIPLY_METHOD_RESOURCE_FACTION, User_m,
                      path='setFraction/{user_id}', http_method='POST',
                      name='users.setFaction')
    def user_set_fraction(self, request):
        return self.users.set_faction(request.user_id, request.faction_id)

    @endpoints.method(ID_RESOURCE, User_m,
                      path='user/{id}', http_method='DELETE',
                      name='users.delUser')
    def user_delete(self, request):
        try:
            return self.users.delete(request.id)
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('User %s not found.' %
                                              (request.id,))

    """
        User Quests
    """
    MULTIPLY_METHOD_RESOURCE_QUEST = endpoints.ResourceContainer(
        user_id=messages.IntegerField(2, variant=messages.Variant.INT64, required=True),
        quest_id=messages.IntegerField(3, variant=messages.Variant.INT64, required=True)
    )

    @endpoints.method(ID_RESOURCE, SolvedQuestsCollection_m,
                      path='userPoints/{id}', http_method='GET',
                      name='users.getPoints')
    def user_get_points(self, request):
        # try:
        return self.users.get_points(request.id)
        # except (IndexError, TypeError):
        #     raise endpoints.NotFoundException('User %s not found.' %
        #                                       (request.id))

    @endpoints.method(ID_RESOURCE, SolvedQuestSum_m,
                      path='userPointsSum/{id}', http_method='GET',
                      name='users.getPointsSum')
    def user_get_points_sum(self, request):
        try:
            return self.users.get_points_sum_m(request.id)
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('User %s not found.' %
                                              (request.id))

    @endpoints.method(MULTIPLY_METHOD_RESOURCE_QUEST, SolvedQuest_m,
                      path='givePoints/{user_id}', http_method='POST',
                      name='users.givePoints')
    def user_give_points(self, request):
        return self.users.add_points(request.user_id, request.quest_id)

    @endpoints.method(MULTIPLY_METHOD_RESOURCE_QUEST, SolvedQuest_m,
                      path='questSolved/{user_id}', http_method='POST',
                      name='users.questSolved')
    def user_quest_solved(self, request):
        return self.users.solve_quest(request.user_id, request.quest_id)

    """
        Quests
    """
    @endpoints.method(message_types.VoidMessage, QuestsCollection_m,
                      path='quest', http_method='GET',
                      name='quests.list')
    def quests_list(self, unused_request):
        return self.quests.list()

    ID_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            id=messages.IntegerField(1, variant=messages.Variant.INT64)
    )

    @endpoints.method(ID_RESOURCE, QuestsCollection_m,
                      path='freactionQuest/{id}', http_method='GET',
                      name='quests.listFractionQuests')
    def quests_list_fraction(self, request):
        return self.quests.list_by_fraction(request.id)

    ID_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            id=messages.IntegerField(1, variant=messages.Variant.INT64)
    )

    @endpoints.method(ID_RESOURCE, Quest_m,
                      path='quest/{id}', http_method='GET',
                      name='quests.getQuest')
    def quest_get(self, request):
        try:
            return self.quests.get(request.id)
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Quest %s not found.' %
                                              (request.id))

    MULTIPLY_METHOD_RESOURCE = endpoints.ResourceContainer(Quest_m)
        # ,
        # name=messages.StringField(2, variant=messages.Variant.STRING,
        #                             required=True))

    @endpoints.method(MULTIPLY_METHOD_RESOURCE, Quest_m,
                      path='quest', http_method='POST',
                      name='quests.addQuest')
    def quest_add(self, request):
        return self.quests.create(request.name, request.faction, request.points)
        #return User(name=request.name) #* request.name

    @endpoints.method(ID_RESOURCE, Quest_m,
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
    @endpoints.method(message_types.VoidMessage, FactionStats_m,
                      path='stats', http_method='GET',
                      name='faction.Stats')
    def faction_stats_get(self, request):
        try:
            return self.game.stats()
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Quest %s not found.')

    LIMIT = endpoints.ResourceContainer(
            message_types.VoidMessage,
            limit=messages.IntegerField(1, variant=messages.Variant.INT64))

    @endpoints.method(LIMIT, Leaderboard_m,
                      path='leaderboard/{limit}', http_method='GET',
                      name='leaderboard.get')
    def leaderboard_get(self, request):
        try:
            return self.game.leaderboard(request.limit)
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Quest %s not found.')


APPLICATION = endpoints.api_server([DevfestCdhApi])