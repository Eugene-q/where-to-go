from django.db import models
from geojson import Feature, Point

class Location(models.Model):
    title = models.CharField(max_length=300)
    place_id = models.CharField(max_length=100, unique=True, default='placeId')
    description_short = models.TextField(default='Описание')
    description_long = models.TextField(default='Подробное описание')
    coordinates_lng = models.FloatField()
    coordinates_lat = models.FloatField()
    details_url = "{% static 'places/moscow_legends.json'%}"
    
    def __str__(self):
        return self.title
        
    def get_place(self):
        return Feature(geometry=Point([self.coordinates_lng, self.coordinates_lat]), 
                       properties={"title": self.title,
                                   "placeId": self.place_id,
                                   "detailsUrl": self.details_url,
                       })

class Image(models.Model):
    title = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=0)
    image = models.ImageField()
    
    def __str__(self):
        return self.title
