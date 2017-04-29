# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-25 17:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_secret_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secret',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='secret',
            name='user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='salt',
        ),
        migrations.DeleteModel(
            name='Secret',
        ),
    ]
