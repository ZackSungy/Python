# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toorder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buiness',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='buiness',
            name='num',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]