# Generated by Django 3.1.3 on 2021-02-28 16:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0011_auto_20210228_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 16, 36, 2, 425471), null=True),
        ),
    ]
