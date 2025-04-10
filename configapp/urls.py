# movie_app/urls.py
from multiprocessing.reduction import register
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ActorApi, MovieApi, CommitApiView

router = DefaultRouter()
router.register('actor', ActorApi, basename='actor')
router.register('movie', MovieApi, basename='movie')
router.register('commit', CommitApiView, basename='commit')


urlpatterns = [
    path('actors/', ActorApi.as_view(), name='actor-list-create'),
    path('movies/', MovieApi.as_view(), name='movie-list-create'),
    path('commits/', CommitApiView.as_view(), name='commit-list-create'),
]
