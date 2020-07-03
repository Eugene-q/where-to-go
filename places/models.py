from django.db import models
from geojson import Feature, Point

class Location(models.Model):
    title = models.CharField(max_length=300)
    place_id = models.CharField(max_length=100, unique=True, default="placeId")
    coordinates_lng = models.FloatField()
    coordinates_lat = models.FloatField()
    details_url = "{% static 'places/moscow_legends.json'%}"#models.FileField(upload_to='json/moscow_legends.json')
    
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
    image = models.ImageField()
    
    def __str__(self):
        return self.title
