# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-21 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190221_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='entrega_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
