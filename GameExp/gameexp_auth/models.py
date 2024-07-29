from django.db import models
from django.contrib.auth.models import User

class GameExpUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, default='undefined', blank=True, null=True)
    web_url = models.CharField(max_length=255, default='undefined', blank=True, null=True)
    twitter_url = models.CharField(max_length=50, default='undefined', blank=True, null=True)
    avatar = models.ImageField(upload_to='user-avatars/', blank=True, null=True)

    def generate_twitter_url(self):
        return f'https://x.com/{self.twitter_url}'
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
