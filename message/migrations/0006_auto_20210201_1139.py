# Generated by Django 3.1.3 on 2021-02-01 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_auto_20210201_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamViewerTokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire_on', models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 1, 11, 39, 57, 810712), null=True)),
                ('access_token', models.CharField(blank=True, max_length=1200, null=True)),
                ('refresh_token', models.CharField(blank=True, max_length=1200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='conversation',
            name='end_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 1, 11, 39, 57, 808236), null=True),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='last_message_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 1, 11, 39, 57, 808137), null=True),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='start_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 1, 11, 39, 57, 808219), null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 1, 11, 39, 57, 809703), null=True),
        ),
    ]
