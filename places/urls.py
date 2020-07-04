from django.urls import path
from . import views
from places.views import map_view
from places.views import location_view

urlpatterns = [
    path('', map_view),
    path('<place_id>/', location_view),
]
