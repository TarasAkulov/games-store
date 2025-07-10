from django.shortcuts import render
from django.db.models import Q
from db.models import Game, Genre, Review, SellItem, SystemRequirement

PLATFORMS = {
    "PC": ["Windows", "Mac", "Linux"],
    "Mobile": ["Android", "Ios"],
    "Console": ["Xbox", "Playstation"],
}

def games(request):
    genres = Genre.objects.all()
    search_query = request.GET.get("search", "")

    if request.method == "GET":
        games = Game.objects.all()
        if search_query:
            games = games.filter(title__icontains=search_query)
        return render(request, "games.html", {"platforms": PLATFORMS.keys(), "genres": genres, "games": games})
    
    elif request.method == "POST":
        selected_platforms_names = request.POST.getlist("platforms[]")
        selected_genres_names = request.POST.getlist("genres[]")
        search_query = request.POST.get("search", "")

        filtered_genres = Genre.objects.filter(name__in=selected_genres_names)

        system_req_query = Q()
        for name in selected_platforms_names:
            for system in PLATFORMS[name]:
                system_req_query |= Q(os__iexact=system)
        system_requierments = SystemRequirement.objects.filter(system_req_query)

        games = Game.objects.all()

        if selected_genres_names:
            games = games.filter(genre__in=filtered_genres)
        
        if selected_platforms_names:
            games = games.filter(optimal_requierments=system_requierments).distinct()

        if search_query:
            games = games.filter(name__icontains=search_query).distinct()
        
        return render(request, "games.html", {"platforms": PLATFORMS.keys(), "genres": genres, "games": games})

def game_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    reviews = Review.objects.filter(game=game).order_by("-created_at")
    sell_items = SellItem.objects.filter(game=game)
    return render(request, "game.html", {"game": game, "reviews": reviews, "sell_items": sell_items})