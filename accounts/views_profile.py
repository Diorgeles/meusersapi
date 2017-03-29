# -*- coding:utf-8 -*-
from __future__ import unicode_literals

# Stdlib imports
import datetime
# Core Django imports
from django.db.models import Q

# Third-party app imports
from raven.contrib.django.raven_compat.models import client

from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,

)
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)

# Imports from your apps
from .models import CustomUser, Profile
from addresses.models import Address
from .serializers import (
    ProfileSerializer,
    UserShortListSerializer,
    UserCreateUpdateSerializer
)

from api.pagination import DefaultPageNumberPagination


class ProfileMeView(APIView):
    """
    get:
    Return the profile of user token session or jwt.
    """
    def get(self, request, format=None):
        try:
            user = CustomUser.objects.get(email=self.request.user.email)
        except Exception:
            return Response(
                {
                    'errors': 'Não encontrados um usuário com sessão ativa'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UserShortListSerializer(user)
        return Response(serializer.data)


class ProfileDetailCodeView(RetrieveAPIView):
    """
    get:
    Return a profile info by code.
    """

    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = ProfileSerializer

    lookup_field = 'code'

    def get_queryset(self, *args, **kwargs):

        qs = Profile.objects.select_related('user').all()

        return qs
