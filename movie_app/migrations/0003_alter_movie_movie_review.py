# Generated by Django 4.1.2 on 2022-10-17 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_movie_movie_review_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='review', to='movie_app.review'),
        ),
    ]
