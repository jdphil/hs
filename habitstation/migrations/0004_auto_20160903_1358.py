# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-03 13:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habitstation', '0003_remove_user_habit_activity_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_habit',
            old_name='user',
            new_name='habit_user',
        ),
    ]