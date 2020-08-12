from django.core.management.base import BaseCommand, CommandError
from places.models import Location
import json
import os

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('load_dir_path', type=str)
    def handle(self, *args, **options):
        load_dir = options['load_dir_path']
        for json_filename in os.listdir(load_dir):
            with open(os.path.join(load_dir, json_filename), 'r') as place_json:
                place = json.load(place_json)
            obj, created = Location.objects.get_or_create(
                                title=place['title'],
                                description_short=place['description_short'],
                                description_long=place['description_long'],
                                coordinates_lng=place['coordinates']['lng'],
                                coordinates_lat=place['coordinates']['lat'],
                                )
            if created:
                self.stdout.write(self.style.SUCCESS('place {} created sucsessfully'.format(place['title'])))