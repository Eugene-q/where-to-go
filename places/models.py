from django.db import models
from geojson import Feature, Point
from tinymce.models import HTMLField

class Location(models.Model):
    title = models.CharField(max_length=300)
    description_short = models.TextField(default='Описание')
    description_long = HTMLField(default='Подробное описание')
    coordinates_lng = models.FloatField()
    coordinates_lat = models.FloatField()
    details_url = ''
    
    def __str__(self):
        return self.title
        
    def get_place(self):
        return Feature(geometry=Point([self.coordinates_lng, self.coordinates_lat]), 
                       properties={"title": self.title,
                                   "placeId": self.id,
                                   "detailsUrl": self.details_url,
                       })

class Image(models.Model):
    title = models.CharField(max_length=100, default='Image')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=0)
    image = models.ImageField()
    position = models.PositiveIntegerField(default=0, blank=False, null=False)
    
    def __str__(self):
        return self.title
    
    class Meta(object):
        ordering = ('position',)
