from rest_framework import serializers
from .models import GameExpUser

class GameExpProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameExpUser
        fields = '__all__'
        