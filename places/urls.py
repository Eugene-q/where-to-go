from django.urls import path
from . import views
from places.views import map_view

urlpatterns = [
    path('', map_view),
]
