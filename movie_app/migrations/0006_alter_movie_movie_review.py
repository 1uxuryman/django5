# Generated by Django 4.1.2 on 2022-10-17 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_alter_movie_movie_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Review', to='movie_app.review'),
        ),
    ]
