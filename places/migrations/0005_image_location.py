# Generated by Django 3.0.7 on 2020-07-10 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20200711_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='places.Location'),
        ),
    ]
