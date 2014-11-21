__author__ = 'tivvit'

from google.appengine.ext import ndb


class SolvedQuest(ndb.Model):
    id_user = ndb.IntegerProperty()
    id_quest = ndb.IntegerProperty()
    points = ndb.IntegerProperty()
    inserted = ndb.DateTimeProperty(auto_now_add=True)

    def add_points(self, user_id, points):
        solved = SolvedQuest(
            id_user=user_id,
            points=points,
        )

        solved.put()
        return solved

    def solve_quest(self, user_id, quest_id, points):
        solved = SolvedQuest(
            id_user=user_id,
            id_quest=quest_id,
            points=points
        )

        solved.put()
        return solved

    def get_user_points_sum(self, user_id):
        sum = 0
        for solved in SolvedQuest.query(SolvedQuest.id_user == user_id).fetch():
            sum += int(solved.points)

        return sum

    def get_user_points_list(self, user_id):
        return SolvedQuest.query(SolvedQuest.id_user == user_id).fetch()

    def delete(self, id):
        return ndb.Key(SolvedQuest, id).delete()
