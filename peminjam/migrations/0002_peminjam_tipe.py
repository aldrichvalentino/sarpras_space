# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peminjam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peminjam',
            name='tipe',
            field=models.CharField(choices=[(b'Fakultas', b'Fakultas'), (b'UKA', b'UKA'), (b'UKM', b'UKM')], default=b'UKM', max_length=50),
        ),
    ]