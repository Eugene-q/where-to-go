from django.contrib import admin
from .models import Location, Image
from django.utils.html import format_html
from django.utils.safestring import mark_safe

class ImageInLine(admin.TabularInline):
    fields = ('title', 'image', 'get_preview', 'position')
    readonly_fields = ('get_preview',)
    model = Image
    
    def get_preview(self, obj):
        raito = obj.image.width / obj.image.height
        return format_html('<img src="{url}" width="{width}" height={height} />',
                            url=obj.image.url,
                            width=200 * raito,
                            height=200,
                            )

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [
        ImageInLine,
    ]

admin.site.register(Image)
