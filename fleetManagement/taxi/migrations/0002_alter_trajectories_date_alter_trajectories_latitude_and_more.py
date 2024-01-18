# Generated by Django 5.0.1 on 2024-01-18 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trajectories',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='trajectories',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trajectories',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
