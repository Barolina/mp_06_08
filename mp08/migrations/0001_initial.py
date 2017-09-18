# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 22:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MethodMp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='описание метода')),
            ],
            options={
                'verbose_name': 'Метод образования',
            },
        ),
        migrations.CreateModel(
            name='PackageMp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('version_mp', models.CharField(default='06', max_length=255)),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mp08.MethodMp')),
            ],
            options={
                'verbose_name': 'Проект',
            },
        ),
    ]
