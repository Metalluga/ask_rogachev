# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20161113_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='questions.Question'),
            preserve_default=False,
        ),
    ]