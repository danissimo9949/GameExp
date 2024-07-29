from django.urls import path
from .views import RetrieveUserProfile

urlpatterns = [
    path('<str:username>', RetrieveUserProfile.as_view(), name='user-profile'),
]