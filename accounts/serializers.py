# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports

# Core Django imports
from django.utils.text import slugify
# Third-party app imports
from rest_framework import serializers
from rest_framework import permissions

# Imports from your apps
from accounts.models import (
    CustomUser, Profile
)

from addresses.serializers import AddressSerializer


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'name', 'code']


class UserShortListSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    name = serializers.SerializerMethodField()
    token = serializers.SerializerMethodField()

    address = AddressSerializer(many=True)

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
            'address',
            'token',
        ]


class UserListSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(required=False)

    name = serializers.SerializerMethodField()

    token = serializers.SerializerMethodField()

    address = AddressSerializer(many=True)

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
            'address',
            'token',
            'created',
            'modified',
            'last_login'
        ]


class UserCreateUpdateSerializer(serializers.ModelSerializer):

    name = serializers.CharField()

    password = serializers.CharField(
        style={'input_type': 'password'}
    )

    # Adress
    # Não consegui realizar um post atraves de um DictField
    # e até mesmo atraves do AddressSerializer

    street = serializers.CharField()
    number = serializers.CharField()
    district = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    country = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = [
            'name',
            'email',
            'password',
            'street',
            'number',
            'district',
            'city',
            'state',
            'country'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        """
        Valida email

        Acabou que não esta sendo utilizado pois o model do django faz a
        validação automaticamente
        """
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email ja existe")
        return value
