# Generated by Django 3.0.8 on 2021-11-01 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_availabledestination_city'),
        ('auth', '0011_update_proxy_permissions'),
        ('user', '0006_auto_20211101_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.FloatField(blank=True, null=True, verbose_name='Salary')),
                ('join_data', models.DateField(blank=True, null=True)),
                ('leave_data', models.DateField(blank=True, null=True)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Faculty', verbose_name='Member of Faculty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'verbose_name': 'Staff User',
                'verbose_name_plural': 'Staff Users',
                'ordering': ['id'],
            },
        ),
    ]
