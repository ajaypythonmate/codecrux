# Generated by Django 3.1.7 on 2021-03-06 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0013_auto_20210228_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 6, 11, 20, 22, 390885), null=True),
        ),
    ]
