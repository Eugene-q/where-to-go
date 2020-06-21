from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from datacenter.map_view import map_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', map_view),
]
