from django.shortcuts import render
from .models import Location
from geojson import FeatureCollection
#import pprint

def map_view(request):
    features = [location.get_place() for location in Location.objects.all()]
    context = {
        "locations" : FeatureCollection(features)
        }
    #pprint.pprint(context)
    return render(request, 'map.html', context)

