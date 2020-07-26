from django.urls import path
from . import views
from places.views import map_view, location_view

urlpatterns = [
    path('', map_view),
    path('<id>/', location_view, name='location_details_url'),
]
