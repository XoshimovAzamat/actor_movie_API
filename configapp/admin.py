from django.contrib import admin
from django.template.context_processors import request

from configapp.models import Actors, Movie

admin.site.register([Movie, Actors])