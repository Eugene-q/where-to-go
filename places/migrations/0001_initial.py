# Generated by Django 3.0.7 on 2020-06-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('coordinates_lng', models.FloatField()),
                ('coordinates_lat', models.FloatField()),
            ],
        ),
    ]
