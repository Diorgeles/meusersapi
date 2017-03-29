# -*- coding:utf-8 -*-
from __future__ import unicode_literals

# Stdlib imports


# Core Django imports
from django.contrib import admin
from django.utils.translation import ugettext as _

# Third-party app imports

# Realative imports of the 'app-name' package
from .models import (
    Address

)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """
    Classe admin para o model de endereços do usuario
    """
    list_display = (
        'user',
        'street_full_name',
        'city',
        'created'
    )

    def street_full_name(self, obj):
        return '{},{},{}'.format(
            obj.street,
            obj.number,
            obj.district
        )

    street_full_name.short_description = 'Endereço completo'

    date_hierarchy = 'created'
    search_fields = ('street', 'district', 'city', 'created', )
    list_filter = ('created', )
