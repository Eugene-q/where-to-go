from django.shortcuts import render
from .models import Location, Image 
from geojson import FeatureCollection
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json 

def map_view(request):
    features = [location.get_place() for location in Location.objects.all()]
    context = {
        "locations" : FeatureCollection(features)
        }
    return render(request, 'map.html', context)

def location_view(request, id):
    place = get_object_or_404(Location, id=id)
    images = []
    for image in Image.objects.filter(location=place.id):
        images.append(str(image.image.file))
    print(images)
    response_data = {
                'title' : place.title,
                'imgs' : images,
                'description_short' : place.description_short,
                'description_long' : place.description_long,
                'coordinates' : {
                            'lat' : place.coordinates_lat,
                            'lng' : place.coordinates_lng,
                            }
                }
    json_dumps_params = {
                'ensure_ascii' : False,
                'indent' : 4,
                }
    response = JsonResponse(response_data, json_dumps_params=json_dumps_params)
    return response 
    
