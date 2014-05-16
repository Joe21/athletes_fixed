from django.test import TestCase
from crud.models import Athlete

class AthleteTest(TestCase):
    def test_first_name(self):
        """
        .first_name will return the correct first name
        """
        john_starks = Athlete(first_name="John", last_name="Starks", sport="NBA", recommendation="a")
        self.assertEqual(john_starks.first_name, "John")

    def test_last_name(self):
        """
        .last_name will return the correct last name
        """
        john_starks = Athlete(first_name="John", last_name="Starks", sport="NBA", recommendation="a")
        self.assertEqual(john_starks.last_name, "Starks")

    def test_sport(self):
        """
        .sport will return the correct sport
        """
        john_starks = Athlete(first_name="John", last_name="Starks", sport="NBA", recommendation="a")
        self.assertEqual(john_starks.sport, "NBA")

    def test_recommendation(self):
        """
        .recommendation will return the correct recommendation choice
        """
        john_starks = Athlete(first_name="John", last_name="Starks", sport="NBA", recommendation="a")
        self.assertEqual(john_starks.recommendation, "a")

    def test_recommendation_value(self):
        """
        .get_recommendation_display() will return the correct value of the recommendation choice
        """
        john_starks = Athlete(first_name="John", last_name="Starks", sport="NBA", recommendation="a")
        self.assertEqual(john_starks.get_recommendation_display(), "Hire Joe IMMEDIATELY!")