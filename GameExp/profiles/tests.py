from django.test import TestCase
from django.contrib.auth.models import User
from .models import GameExpUser

class GameExpProfileTest(TestCase):

    def test_generate_twitter_url_funtion(self):
        user = User.objects.create(
            username = 'test_user2',
            password = 'testpassword2',
            email = 'testemail1@gmail.com',
        )
        game_exp_user = GameExpUser(user=user, twitter_login = 'danissimoSs')
        twitter_url = game_exp_user.generate_twitter_url()
        self.assertEqual(twitter_url, 'https://x.com/danissimoSs')


    def test_public_profile_url_equal(self):
        user = User(username='DanissimoTest')
        username = user.username.lower()
        self.assertEqual(username, 'danissimotest')

    
    def test_create_user_profile(self):
        user = User.objects.create(
            username='test_user', 
            password='testpassword228', 
            email = 'testemail@gmail.com',
        )
        game_exp_user = GameExpUser.objects.get(user=user)
        self.assertIsNotNone(game_exp_user)
        self.assertEqual(game_exp_user.user, user)
    

