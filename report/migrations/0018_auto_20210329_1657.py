# Generated by Django 3.1.3 on 2021-03-29 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0017_auto_20210310_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 29, 16, 57, 30, 999889), null=True),
        ),
    ]
