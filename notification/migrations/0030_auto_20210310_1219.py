# Generated by Django 3.1.3 on 2021-03-10 12:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0029_auto_20210310_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 10, 12, 19, 4, 907572), null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 10, 12, 19, 4, 906985), null=True),
        ),
    ]
