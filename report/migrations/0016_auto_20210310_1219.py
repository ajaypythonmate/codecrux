# Generated by Django 3.1.3 on 2021-03-10 12:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0015_auto_20210310_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 10, 12, 19, 4, 905112), null=True),
        ),
    ]