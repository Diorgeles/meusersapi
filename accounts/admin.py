# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports


# Core Django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext as _
# Third-party app imports
from rest_framework.authtoken.admin import TokenAdmin
# Realative imports of the 'app-name' package
from .models import (
    CustomUser, Profile
)
from .forms import CustomUserCreationForm, CustomUserChangeForm


class UserProfileInline(admin.TabularInline):
    model = Profile
    can_delete = False


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # formulario para adicionar usuarios palestrantes
    add_form = CustomUserCreationForm

    # formulario para alterar usuarios
    form = CustomUserChangeForm

    inlines = (UserProfileInline,)

    # campos a serem exibidos na tabela
    list_display = (
        'email',
        'is_staff',
        'created'
    )
    # campos que podem ser filtrados
    list_filter = (
        'created',
        'is_staff',
        'is_superuser',
        'is_active',
        'groups'
    )

    # campos que utilizam buscas no model
    search_fields = (
        'email',
        'created',
    )
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'password'
                )
            }
        ),
        (
            _(u'Permissões'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            }
        ),
        (
            _(u'Datas importantes'),
            {
                'fields': (
                    'last_login',
                )
            }
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    ordering = (
        'email',
    )

    date_hierarchy = 'created'


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    # campos a serem exibidos na tabela
    list_display = (
        'user',
        'name',
        'created'
    )
    # campos que podem ser filtrados
    list_filter = (
        'created',
        'kind_user',
    )


TokenAdmin.raw_id_fields = ('user',)
