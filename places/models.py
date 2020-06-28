from django.db import models

class Location(models.Model):
    title = models.CharField(max_length=300)
    description_short = models.TextField()
    description_long = models.TextField()
    coordinates_lng = models.FloatField()
    coordinates_lat = models.FloatField()
    
    def __str__(self):
        return self.title
        

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    
    def __str__(self):
        return self.title
