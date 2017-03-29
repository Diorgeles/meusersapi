# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports

# Core Django imports
from django.utils.text import slugify
# Third-party app imports
from rest_framework import serializers


# Imports from your apps
from accounts.models import (
    CustomUser, Profile
)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'name', 'code']


class UserShortListSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(required=False)

    name = serializers.SerializerMethodField()

    token = serializers.SerializerMethodField()

    def get_name(self, obj):
        return '{}'.format(
            obj.get_full_name()
        )

    def get_token(self, obj):
        return '{}'.format(
            obj.get_token()
        )

    class Meta:
        model = CustomUser
        fields = [
            'code',
            'email',
            'profile',
            'name',
            'token',
            'created',
            'modified',
            'last_login'
        ]
