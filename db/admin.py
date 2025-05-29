from django.contrib import admin
from .models import Game, Genre, Developer, SystemRequirement

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Developer)
admin.site.register(SystemRequirement)