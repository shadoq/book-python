# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontakt', '0002_adress_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_of_birth',
            field=models.DateField(default=None, verbose_name='Date of Birth', blank=True, null=True),
            preserve_default=False,
        ),
    ]
