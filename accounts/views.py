# -*- coding:utf-8 -*-
from __future__ import unicode_literals

# Stdlib imports
import datetime
# Core Django imports
from django.db.models import Q

# Third-party app imports
from raven.contrib.django.raven_compat.models import client

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
from .models import CustomUser
from .serializers import (
    ProfileSerializer,
    UserShortListSerializer
)

from api.pagination import DefaultPageNumberPagination


class UserListView(ListAPIView):
    """
    List all users
    """

    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = UserShortListSerializer

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ['name', 'email']

    pagination_class = DefaultPageNumberPagination

    def get_queryset(self, *args, **kwargs):

        qs = CustomUser.objects.all()

        query = self.request.GET.get('q')

        if ('q' in self.request.GET) and query.strip():
            qs = qs.filter(
                Q(name__icontains=query)
            )

        return qs
