# Generated by Django 3.1.3 on 2021-03-29 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0031_auto_20210310_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 29, 16, 57, 31, 1618), null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 29, 16, 57, 31, 1150), null=True),
        ),
    ]
