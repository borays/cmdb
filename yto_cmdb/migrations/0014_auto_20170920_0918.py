# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yto_cmdb', '0013_auto_20170920_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vm',
            name='date_added',
            field=models.DateField(),
        ),
    ]
