# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-23 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licitacion', '0005_auto_20180623_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licitacion',
            name='publicada',
            field=models.BooleanField(default=True),
        ),
    ]