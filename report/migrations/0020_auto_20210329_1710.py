# Generated by Django 3.1.3 on 2021-03-29 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0019_auto_20210329_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 29, 17, 9, 56, 829024), null=True),
        ),
    ]
