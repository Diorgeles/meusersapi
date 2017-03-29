# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 17:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='endereço de email')),
                ('is_staff', models.BooleanField(default=False, help_text='Indica que usuário consegue acessar este site de administração.', verbose_name='membro da equipe')),
                ('is_active', models.BooleanField(default=True, help_text='Indica que o usuário será tratado como ativo. Ao invés de excluir contas de usuário, desmarque isso.', verbose_name='ativo')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de registro')),
                ('is_admin', models.BooleanField(default=False, help_text='Designa este usuário como administrador.', verbose_name='Administrador')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Usuários',
                'verbose_name': 'Usuário',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome completo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name_plural': 'Perfis',
                'verbose_name': 'Perfil',
                'permissions': (('can_access_administration', 'Acesso aos menus de administração'), ('can_access_user', 'Acesso aos menus de usuários'), ('can_change_own_password', 'Alterar a propria senha'), ('can_access_group', 'Acesso aos menus de grupos de usuários')),
            },
        ),
    ]
