# Generated by Django 4.1.7 on 2023-05-23 08:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_alter_restaurant_date_of_establishment'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='type',
            field=models.CharField(blank=True, choices=[('Iranian', 'Iranian'), ('Foreign', 'Foreign')], max_length=255),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='date_of_establishment',
            field=models.DateField(default=datetime.date(2023, 5, 23)),
        ),
    ]
