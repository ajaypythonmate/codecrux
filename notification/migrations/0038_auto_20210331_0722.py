# Generated by Django 3.1.3 on 2021-03-31 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0037_auto_20210331_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 7, 22, 27, 791473), null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 7, 22, 27, 790912), null=True),
        ),
    ]
