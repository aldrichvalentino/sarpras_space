# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-01 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import peminjaman.models


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0003_peminjaman_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='peminjaman',
            name='foto_bon',
            field=models.ImageField(blank=True, max_length=500, upload_to=peminjaman.models.bon_foto_dir),
        ),
    ]
