# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 06:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toorder', '0003_auto_20170731_0519'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Buiness',
            new_name='Business',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Buiness',
            new_name='Business',
        ),
    ]
