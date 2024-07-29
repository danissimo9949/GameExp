from django.http import Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import GameExpProfileSerializer
from .models import GameExpUser

class RetrieveUserProfile(generics.RetrieveAPIView):
    serializer_class = GameExpProfileSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        username = self.kwargs.get('username')

        try:
            profile = GameExpUser.objects.get(user__username = username)
            return profile
        except GameExpUser.DoesNotExist:
            raise Http404("Profile don't exist")
