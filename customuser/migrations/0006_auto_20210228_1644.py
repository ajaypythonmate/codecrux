# Generated by Django 3.1.3 on 2021-02-28 16:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0005_auto_20210228_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 16, 44, 32, 135037), null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_seen',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 16, 44, 32, 134977), null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
    ]
