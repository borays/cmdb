# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yto_cmdb', '0011_auto_20170920_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmdb',
            name='ma_date',
            field=models.DateTimeField(),
        ),
    ]