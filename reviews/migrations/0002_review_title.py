# Generated by Django 5.0.4 on 2024-04-24 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.ManyToManyField(related_name='movies', to='movies.movie'),
        ),
    ]
