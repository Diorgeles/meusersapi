# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': (('can_access_users', 'Acesso aos usuarios'),), 'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
