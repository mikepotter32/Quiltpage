# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170226_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quilt',
            name='pic',
            field=models.ImageField(upload_to='media/'),
        ),
    ]