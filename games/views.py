from django.shortcuts import render

def games(request):
    return render(request, "games.html")

def game_detail(request, game_id):
    print(f"Game ID: {game_id}")
    return render(request, "game.html")