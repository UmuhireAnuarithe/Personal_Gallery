# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-10 09:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Photos', '0002_auto_20191010_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='lacation',
            new_name='category',
        ),
    ]