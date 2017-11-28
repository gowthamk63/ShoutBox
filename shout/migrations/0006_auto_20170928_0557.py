# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-28 05:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shout', '0005_auto_20161110_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('following', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Likers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liker', models.CharField(max_length=100)),
                ('shout_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif_text', models.CharField(max_length=300)),
                ('when', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='NotifMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('seen', models.BooleanField(default=False)),
                ('notif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shout.Notification')),
            ],
        ),
        migrations.AddField(
            model_name='shouts',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dateOfBirth',
            field=models.DateField(default=datetime.date(2017, 9, 28)),
        ),
    ]
