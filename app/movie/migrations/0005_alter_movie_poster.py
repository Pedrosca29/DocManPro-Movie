# Generated by Django 4.2.6 on 2023-10-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_movie_poster_alter_movie_url_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(max_length=200, upload_to='', verbose_name='Póster'),
        ),
    ]
