# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-29 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='year_course',
            field=models.CharField(choices=[('0', 'Choose your option'), ('2018', '2018'), ('2019', '2019')], default=0, max_length=50),
        ),
    ]
