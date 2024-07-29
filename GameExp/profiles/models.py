from django.db import models
from django.contrib.auth.models import User

class GameExpUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_two_auth = models.BooleanField(default=False)
    additional_email = models.EmailField(blank=True)

    display_name = models.CharField(max_length=100, blank=True)
    public_url = models.URLField(max_length=255, blank=False)
    web_url = models.URLField(max_length=255, blank=True)
    twitter_login = models.CharField(max_length=50, blank=True)
    twitter_url = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True)
    background_img = models.ImageField(upload_to='users/background-images/', blank=True)
    profile_content = models.TextField(blank=True)

    def set_display_name(self):
        return self.user.username
        

    def generate_twitter_url(self):
        if self.twitter_login:
            return f'https://x.com/{self.twitter_login}'

    def generate_public_url(self):
        correct_username = self.user.username.lower()
        return f'https://host/api/profiles/{correct_username}'
        
        
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
