# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-28 23:02
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0037_auto_20160528_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
