# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-30 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0047_researchstudent_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchstudent',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=b'iiits/static/iiits/files/research/portfolio/'),
        ),
    ]