# Generated by Django 4.0.4 on 2022-05-16 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=250)),
                ('content', models.CharField(max_length=2050)),
                ('time_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
