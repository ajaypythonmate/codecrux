# Generated by Django 3.1.3 on 2021-01-16 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20210116_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='last_message_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 16, 11, 38, 25, 236927), null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 16, 11, 38, 25, 238587), null=True),
        ),
    ]