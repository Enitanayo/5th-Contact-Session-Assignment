from django.urls import path
from .views import media_gallery

urlpatterns = [
    path("", media_gallery, name="media"),
]