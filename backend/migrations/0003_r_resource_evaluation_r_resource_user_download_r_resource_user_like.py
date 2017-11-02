# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-02 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_evaluation'),
    ]

    operations = [
        migrations.CreateModel(
            name='R_Resource_Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_id', models.PositiveIntegerField()),
                ('eva_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='R_Resource_User_Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('resource_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='R_Resource_User_Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('resource_id', models.PositiveIntegerField()),
            ],
        ),
    ]
