from django.shortcuts import render
from db.models import Game

def index(request):
    games = Game.objects.all()[:3]
    context = {
        'games': games
    }
    return render(request, 'index.html', context)