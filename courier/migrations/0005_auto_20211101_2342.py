# Generated by Django 3.0.8 on 2021-11-01 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0004_auto_20211101_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='deliver_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipent_address', to='courier.CourierAddress', verbose_name='Recipient Address'),
        ),
        migrations.AlterField(
            model_name='courier',
            name='pickup_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_address', to='courier.CourierAddress', verbose_name='Pickup Address'),
        ),
    ]
