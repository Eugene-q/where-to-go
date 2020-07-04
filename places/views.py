from django.shortcuts import render
from .models import Location
from geojson import FeatureCollection
from django.shortcuts import get_object_or_404
#import pprint

def map_view(request):
    features = [location.get_place() for location in Location.objects.all()]
    context = {
        "locations" : FeatureCollection(features)
        }
    #pprint.pprint(context)
    return render(request, 'map.html', context)

def location_view(request, place_id):
    place = get_object_or_404(Location, place_id=place_id)
    context = {
        "place_title" : place.title,
        }
    return render(request, 'location.html', context)
    
