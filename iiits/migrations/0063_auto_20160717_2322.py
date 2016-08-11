# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-17 23:22
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0062_auto_20160717_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchcentre',
            name='background',
        ),
        migrations.AddField(
            model_name='researchcentreprofile',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to=b'iiits/static/iiits/files/research/portfolio/'),
        ),
        migrations.AddField(
            model_name='researchcentreprofile',
            name='faculty',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AlterField(
            model_name='notice',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 24, 23, 22, 38, 374227, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='researchcentreprofile',
            name='description',
            field=ckeditor.fields.RichTextField(default='Sorry, description unavailable at the moment.'),
        ),
        migrations.AlterField(
            model_name='researchcentreprofile',
            name='people',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]