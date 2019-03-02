# Generated by Django 2.1.7 on 2019-03-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_auto_20181107_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='use_consent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registration',
            name='photo_consent',
            field=models.CharField(choices=[('UNKNOWN', 'UNKNOWN'), ('CONSENT', 'CONSENT'), ('NOT_CONSENT', 'NOT_CONSENT')], default='UNKNOWN', max_length=20),
        ),
    ]
