# Generated by Django 3.1.3 on 2021-03-10 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0009_auto_20210310_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 3, 10, 12, 49, 29, 228181), null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_seen',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 10, 12, 49, 29, 228111), null=True),
        ),
    ]
