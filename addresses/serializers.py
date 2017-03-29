# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports

# Core Django imports
from django.utils.text import slugify
# Third-party app imports
from rest_framework import serializers


# Imports from your apps
from .models import (
    Address
)


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = [
            'id',
            'street',
            'number',
            'district',
            'city',
            'state',
            'country',
        ]
