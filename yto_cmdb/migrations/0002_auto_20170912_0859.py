# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yto_cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmdb',
            name='ip_text',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]