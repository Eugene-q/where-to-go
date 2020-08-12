from django.core.management.base import BaseCommand, CommandError
from places.models import Location
import json
import os

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('place_path', type=str)
    def handle(self, *args, **options):
        with open(options['place_path'], 'r') as place_json:
            place = json.load(place_json)
        obj, created = Location.objects.get_or_create(**place)
        if created:
            self.stdout.write(self.style.SUCCESS('place {} created sucsessfully'.format(place['title'])))