# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-18 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20161218_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerlike',
            name='like',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='questionlike',
            name='like',
            field=models.BooleanField(default=True),
        ),
    ]
