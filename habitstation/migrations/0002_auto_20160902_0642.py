# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-02 06:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habitstation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Habit_Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_desc', models.TextField(default='')),
                ('activity_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='user_habit',
            name='habit_desc',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user_habit',
            name='habit_freq',
            field=models.IntegerField(default=7),
        ),
        migrations.AddField(
            model_name='user_habit',
            name='habit_streak',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_habit',
            name='habit',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Habit',
        ),
        migrations.AddField(
            model_name='user_habit_activity',
            name='habit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitstation.User_Habit'),
        ),
        migrations.AddField(
            model_name='user_habit_activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
