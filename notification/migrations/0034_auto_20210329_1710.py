# Generated by Django 3.1.3 on 2021-03-29 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0033_auto_20210329_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 29, 17, 9, 56, 830845), null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 29, 17, 9, 56, 830327), null=True),
        ),
    ]