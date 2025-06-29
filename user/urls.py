from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.user, name="user"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)