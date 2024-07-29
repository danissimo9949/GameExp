from django.test import TestCase

from django.test import TestCase
from .models import GameExpUser

class GameExpUserTest(TestCase):
    def test_generate_twitter_url_funtion(self):
        user = GameExpUser(twitter_url = 'danissimoSs')
        self.assertEqual(user.generate_twitter_url(), 'https://x.com/danissimoSs')
