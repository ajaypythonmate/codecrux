# Generated by Django 3.1.3 on 2021-02-28 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0003_auto_20210228_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 16, 33, 29, 752626), null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_seen',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 16, 33, 29, 752566), null=True),
        ),
    ]
