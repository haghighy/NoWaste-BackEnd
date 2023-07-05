# Generated by Django 4.1.7 on 2023-07-05 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0002_alter_restaurant_date_of_establishment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('room_name', models.CharField(max_length=250)),
                ('sender_type', models.CharField(choices=[('Customer', 'Server'), ('Manager', 'Client')], max_length=8, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='chats', to='User.customer')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='chats', to='User.restaurantmanager')),
            ],
        ),
    ]
