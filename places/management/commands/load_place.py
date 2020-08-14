from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from places.models import Location, Image
import requests, json, os

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('load_dir_path', type=str)
    def handle(self, *args, **options):
        load_dir = options['load_dir_path']
        for json_filename in os.listdir(load_dir):
            with open(os.path.join(load_dir, json_filename), 'r') as place_json:
                place = json.load(place_json)
            new_location, created = Location.objects.get_or_create(
                                title=place['title'],
                                description_short=place['description_short'],
                                description_long=place['description_long'],
                                coordinates_lng=place['coordinates']['lng'],
                                coordinates_lat=place['coordinates']['lat'],
                                )
            if created:
                self.stdout.write(self.style.SUCCESS('{} created sucsessfully'.format(place['title'])))
                for img_link in place['imgs']:
                    response = requests.get(img_link)
                    image_obj = Image.objects.create(location=new_location)
                    image_content = ContentFile(response.content)
                    image_name = img_link.rpartition('/')[2]
                    print('saving', image_name)
                    image_obj.image.save(image_name, image_content, save=True)
            else:
                self.stdout.write(self.style.ERROR('{} already exist in database!'.format(place['title'])))
