# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-15 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_retargeting', '0002_auto_20170415_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='failure',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
