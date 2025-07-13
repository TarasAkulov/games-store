from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.games, name="games"),
    path("search/", views.search, name="search"),
    path("sort_by/", views.sort_by, name="sort_by"),
    path("sort_by_scroll/", views.sort_by_scroll, name="sort_by_scroll"),
    path("<int:game_id>/", views.game_detail, name="game_detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)