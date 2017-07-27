# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_gallery_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='cover',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallery_covers', to='gallery.GalleryPicture'),
        ),
    ]
