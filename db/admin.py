from django.contrib import admin
from .models import Game, Genre, Developer, SystemRequirement, Seller, SellItem, User, Review, UserStory

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Developer)
admin.site.register(SystemRequirement)
admin.site.register(Seller)
admin.site.register(SellItem)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(UserStory)