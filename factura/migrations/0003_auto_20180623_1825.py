# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-23 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0002_factura_checkbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='adjunto',
            field=models.FileField(upload_to='media/'),
        ),
    ]
