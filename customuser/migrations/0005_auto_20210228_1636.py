# Generated by Django 3.1.3 on 2021-02-28 16:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0004_auto_20210228_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 16, 36, 2, 415216), null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_seen',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 16, 36, 2, 415154), null=True),
        ),
    ]
