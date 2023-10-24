# Generated by Django 4.2.6 on 2023-10-24 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Canal')),
                ('description', models.TextField(verbose_name='Descripción del Canal')),
                ('url', models.URLField(verbose_name='URL del Canal')),
            ],
            options={
                'verbose_name': 'Canal',
                'verbose_name_plural': 'Canales',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Género')),
                ('description', models.TextField(verbose_name='Descripción del Género')),
            ],
            options={
                'verbose_name': 'Género',
                'verbose_name_plural': 'Géneros',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('release_date', models.DateField(verbose_name='Fecha de Lanzamiento')),
                ('url_movie', models.URLField(verbose_name='URL de la película')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('poster', models.CharField(max_length=200, verbose_name='Póster')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Slug')),
                ('channel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.channel', verbose_name='Canal Relacionado')),
                ('genre', models.ManyToManyField(to='movie.genre', verbose_name='Géneros')),
            ],
            options={
                'verbose_name': 'Película',
                'verbose_name_plural': 'Películas',
            },
        ),
    ]
