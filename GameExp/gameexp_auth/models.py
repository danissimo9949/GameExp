from django.db import models
from django.contrib.auth.models import User

class GameExpUser(User):
    

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
