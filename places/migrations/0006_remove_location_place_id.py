# Generated by Django 3.0.7 on 2020-07-14 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_image_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='place_id',
        ),
    ]
