# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 15:21
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20171011_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('member', 'member'), ('leader', 'leader'), ('co-leader', 'co-leader'), ('treasurer', 'treasurer'), ('recruiting', 'recruiting'), ('development', 'development'), ('editor', 'editor'), ('retiree', 'retiree'), ('media_relations', 'media_relations'), ('active_retiree', 'active_retiree'), ('alumni', 'alumni'), ('webmaster', 'webmaster'), ('interest_group_admin', 'interest_group_admin'), ('alumni_admin', 'alumni_admin'), ('retiree_email', 'retiree_email'), ('company_admin', 'company_admin'), ('dugnad_admin', 'dugnad_admin'), ('trip_admin', 'trip_admin'), ('sponsor_admin', 'sponsor_admin'), ('social_admin', 'social_admin')], default='member', max_length=30)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField()),
                ('abakus_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.AbakusGroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='membership',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='start_date',
        ),
    ]
