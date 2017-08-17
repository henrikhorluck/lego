# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 17:33
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email', '0002_auto_20170427_1733'),
        ('users', '0017_auto_20170425_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='internal_email',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='email.EmailAddress'),
        ),
    ]