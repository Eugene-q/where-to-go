from django.contrib import admin
from .models import Location, Image

class ImageInLine(admin.TabularInline):
    model = Image
    
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [
        ImageInLine,
    ]

admin.site.register(Image)
