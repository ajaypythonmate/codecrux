# Generated by Django 3.1.3 on 2021-02-10 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0015_auto_20210209_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 10, 17, 10, 44, 33240), null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 10, 17, 10, 44, 32703), null=True),
        ),
    ]
