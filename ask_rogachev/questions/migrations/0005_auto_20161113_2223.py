# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 22:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20161113_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='like',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Like'),
        ),
    ]