# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 18:49
from __future__ import unicode_literals

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='page',
            managers=[
                ('public_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]