# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-28 17:05
from __future__ import unicode_literals

import basis.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('updated_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('deleted', models.BooleanField(default=False, editable=False)),
                ('require_auth', models.BooleanField(default=False, verbose_name='require auth')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('text', models.TextField(blank=True)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('can_edit_groups', models.ManyToManyField(blank=True, related_name='can_edit_article', to='users.AbakusGroup')),
                ('can_edit_users', models.ManyToManyField(blank=True, related_name='can_edit_article', to=settings.AUTH_USER_MODEL)),
                ('can_view_groups', models.ManyToManyField(blank=True, related_name='can_view_article', to='users.AbakusGroup')),
                ('created_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
