from django.urls import path
from .views import *

urlpatterns = [
    path('actors/', ActorApi.as_view(), name='actors'),
    path('movies/', MovieApi.as_view(), name='movies'),
]
