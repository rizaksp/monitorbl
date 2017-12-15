# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lapak', models.CharField(max_length=200, unique=True)),
                ('urlp', models.CharField(max_length=200)),
                ('terjual', models.IntegerField(default=0)),
                ('harga', models.IntegerField(default=0)),
                ('toko', models.CharField(blank=True, max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
