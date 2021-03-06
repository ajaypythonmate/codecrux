# Generated by Django 3.1.3 on 2021-03-31 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0031_auto_20210331_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='end_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 7, 22, 27, 782250), null=True),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='last_message_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 7, 22, 27, 782132), null=True),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='start_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 7, 22, 27, 782234), null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 7, 22, 27, 783770), null=True),
        ),
        migrations.AlterField(
            model_name='teamviewertokens',
            name='expire_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 7, 22, 27, 784922), null=True),
        ),
    ]
