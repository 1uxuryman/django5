# Generated by Django 4.1.2 on 2022-10-17 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0009_remove_movie_descrtiption_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='reviews',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie_app.review'),
        ),
    ]
