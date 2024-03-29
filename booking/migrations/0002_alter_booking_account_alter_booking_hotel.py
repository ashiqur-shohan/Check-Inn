# Generated by Django 5.0.1 on 2024-03-15 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_account_user'),
        ('booking', '0001_initial'),
        ('hotel', '0002_hotel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='account.account'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to='hotel.hotel'),
        ),
    ]
