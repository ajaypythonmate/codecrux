# Generated by Django 3.1.3 on 2021-03-29 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0027_auto_20210329_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='end_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 29, 17, 9, 56, 821705), null=True),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='last_message_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 29, 17, 9, 56, 821602), null=True),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='start_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 29, 17, 9, 56, 821690), null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 29, 17, 9, 56, 823234), null=True),
        ),
        migrations.AlterField(
            model_name='teamviewertokens',
            name='expire_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 29, 17, 9, 56, 824312), null=True),
        ),
    ]