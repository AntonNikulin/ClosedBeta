from django.contrib import admin
from Games.models import Game, Genre, UserRating

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(UserRating)