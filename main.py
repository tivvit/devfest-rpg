__author__ = 'tivvit'

import webapp2
from backend.model.game import Game

class generateLeaderboardHandler(webapp2.RedirectHandler):
    def get(self):
        g = Game()
        g.generateLeaderboard()


app = webapp2.WSGIApplication([
    ('/generateLeaderboard', generateLeaderboardHandler)
], debug=True)
