# Generated by Django 3.1.3 on 2021-02-28 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0024_auto_20210228_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 16, 33, 29, 764779), null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 16, 33, 29, 764314), null=True),
        ),
    ]
