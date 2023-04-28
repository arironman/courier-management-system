# Generated by Django 3.0.8 on 2021-10-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailablePincode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.CharField(blank=True, max_length=10, verbose_name='Pincode')),
            ],
            options={
                'verbose_name': 'Available Pincode',
                'verbose_name_plural': 'Available Pincodes',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.CharField(blank=True, max_length=200, verbose_name='House Number')),
                ('street', models.CharField(blank=True, max_length=200, verbose_name='Street')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='City')),
                ('district', models.CharField(blank=True, max_length=50, verbose_name='District')),
                ('state', models.CharField(blank=True, max_length=50, verbose_name='State')),
                ('pincode', models.CharField(blank=True, max_length=10, verbose_name='Pincode')),
            ],
            options={
                'verbose_name': 'User Address',
                'verbose_name_plural': 'User Addresses',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, max_length=10, verbose_name='Gender'),
        ),
    ]
