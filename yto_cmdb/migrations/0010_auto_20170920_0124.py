# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yto_cmdb', '0009_auto_20170920_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmdb',
            name='ma_date',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cmdb',
            name='mana_user',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cmdb',
            name='model_text',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cmdb',
            name='sn_text',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cmdb',
            name='user_text',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cmdb',
            name='vender_text',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
