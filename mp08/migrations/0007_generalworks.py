# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mp08', '0006_auto_20170903_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralWorks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(default='06', max_length=255)),
                ('pupose', models.CharField(default='06', max_length=255)),
                ('n_doc', models.PositiveIntegerField(blank=True, null=True)),
                ('mp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mp08.PackageMp')),
            ],
            options={
                'verbose_name': 'Общие сведения кадастровых  работ',
            },
        ),
    ]
