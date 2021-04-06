# Generated by Django 3.1.3 on 2021-01-17 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210116_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='educator',
            name='conversation_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='last_seen',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 17, 10, 58, 12, 776258), null=True),
        ),
        migrations.AlterField(
            model_name='educator',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 17, 10, 58, 12, 776775), null=True),
        ),
        migrations.AlterField(
            model_name='educator',
            name='last_seen',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 17, 10, 58, 12, 776828), null=True),
        ),
    ]
