from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from profiles.models import GameExpUser

@receiver(post_save, sender=User)
def create_game_exp_user(sender, instance, created, **kwargs):
    if created:
       user = GameExpUser.objects.create(user=instance)
       user.display_name = user.set_display_name()
       user.public_url = user.generate_public_url()
       user.save()
    
        
