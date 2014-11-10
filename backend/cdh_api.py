__author__ = 'tivvit'

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

from model import User
from model import User
from model import User
from model import User

# class TicTacToeApi(remote.Service):
#
# class YourResponseMessageClass(messages.Message):
#     message = messages.StringField(1)
#
# class YourRequestMessageClass(messages.Message):
#     message = messages.StringField(1)
#
# @endpoints.method(YourRequestMessageClass,
#               YourResponseMessageClass,
#               name='foo.bar', ...)
# def bar(self, request):
#

package = 'Devfest_CDH'

# q = Event.query(ancestor=ndb.Key("events", eventlist), filters=ndb.AND(Event.date != None, Event.date > datetime.now().date())).order(Event.date)
#         events = q.fetch(15)


class Greeting(messages.Message):
    message = messages.StringField(1)


# class User(messages.Message):
#     message = messages.StringField(1)


class GreetingCollection(messages.Message):
    items = messages.MessageField(Greeting, 1, repeated=True)


STORED_GREETINGS = GreetingCollection(items=[
    Greeting(message='hello world!'),
    Greeting(message='goodbye world!'),
])


# user.create()

@endpoints.api(name='devfest_cdh_api', version='v1', description='Devfest 2014 CDH API')
class DevfestCdhApi(remote.Service):

    @endpoints.method(message_types.VoidMessage, GreetingCollection,
                      path='hellogreeting', http_method='GET',
                      name='greetings.listGreeting')
    def greetings_list(self, unused_request):
        return STORED_GREETINGS

    ID_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            id=messages.IntegerField(1, variant=messages.Variant.INT32))

    @endpoints.method(ID_RESOURCE, User,
                      path='user/{id}', http_method='GET',
                      name='users.getUser')
    def greeting_get(self, request):
        try:
            user = User()
            return user.get(1)
            # return STORED_GREETINGS.items[request.id]
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Greeting %s not found.' %
                                              (request.id,))

APPLICATION = endpoints.api_server([DevfestCdhApi])



# q = Event.query(filters=e['url'] == Event.url, ancestor=ndb.Key("events", eventlist))
#
#             eventFound = q.fetch(1)
#             if(len(eventFound) == 0):


# event = Event(parent=ndb.Key("events", eventlist))

#                 event.url = e['url']
#                 event.title = e['title']
#                 event.img = e['img']
#                 event.place = e['place']
#                 event.text = e['text']
#                 event.source = e['source']
#                 if e['date'] is not None:
#                     event.date = e['date']
#                 event.put()