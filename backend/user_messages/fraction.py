__author__ = 'tivvit'

from protorpc import messages

#todo useless use config
class Fraction(messages.Message):
    name = messages.StringField(1)
