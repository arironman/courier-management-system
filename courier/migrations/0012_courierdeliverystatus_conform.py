# Generated by Django 3.0.8 on 2021-11-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0011_auto_20211105_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='courierdeliverystatus',
            name='conform',
            field=models.BooleanField(default=False),
        ),
    ]
