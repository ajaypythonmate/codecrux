# Generated by Django 3.1.3 on 2021-02-28 16:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0017_auto_20210228_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='end_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 16, 30, 2, 618311), null=True),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='last_message_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 16, 30, 2, 618216), null=True),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='start_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 16, 30, 2, 618297), null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 16, 30, 2, 619850), null=True),
        ),
        migrations.AlterField(
            model_name='teamviewertokens',
            name='expire_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 16, 30, 2, 620883), null=True),
        ),
    ]
