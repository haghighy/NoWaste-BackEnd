# Generated by Django 4.1.7 on 2023-04-11 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0003_vc_codes_alter_customer_password"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="email_confirmed",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="vc_code",
        ),
    ]
