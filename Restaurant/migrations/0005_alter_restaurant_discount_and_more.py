# Generated by Django 4.1.7 on 2023-04-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Restaurant", "0004_alter_restaurant_discount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="discount",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=2
            ),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="purches_counts",
            field=models.IntegerField(blank=True, default=100),
        ),
    ]
