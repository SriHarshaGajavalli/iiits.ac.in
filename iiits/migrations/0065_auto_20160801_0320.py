# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-01 03:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0064_auto_20160717_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 8, 3, 20, 11, 215259, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='publication',
            name='authors',
            field=models.TextField(default='NA'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=models.TextField(default='NA'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='link',
            field=models.TextField(default='NA'),
        ),
        migrations.AlterField(
            model_name='researchcentreprofile',
            name='faculty',
            field=models.TextField(default='#'),
        ),
        migrations.AlterField(
            model_name='researchcentreprofile',
            name='people',
            field=models.TextField(default='#'),
        ),
    ]
