from django.urls import path, include
from .views import CreateGameExpUserView

urlpatterns = [
    path('register-user', CreateGameExpUserView.as_view(), name='register-user'), 
]