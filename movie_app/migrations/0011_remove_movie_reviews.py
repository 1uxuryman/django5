# Generated by Django 4.1.2 on 2022-10-17 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_alter_movie_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='reviews',
        ),
    ]
