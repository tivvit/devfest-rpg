__author__ = 'tivvit'

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

import logging

from model import Users
from user_messages import User
from user_messages import UsersCollection

package = 'Devfest_CDH'

users = Users()
# users.create()

@endpoints.api(name='devfest_cdh_api', version='v1', description='Devfest 2014 CDH API')
class DevfestCdhApi(remote.Service):

    @endpoints.method(message_types.VoidMessage, UsersCollection,
                      path='user', http_method='GET',
                      name='users.list')
    def users_list(self, unused_request):
        return users.list()

    ID_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            id=messages.IntegerField(1, variant=messages.Variant.INT32))

    @endpoints.method(ID_RESOURCE, User,
                      path='user/{id}', http_method='GET',
                      name='users.getUser')
    def user_get(self, request):
        try:
            return users.get(request.id)
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('User %s not found.' %
                                              (request.id,))


APPLICATION = endpoints.api_server([DevfestCdhApi])