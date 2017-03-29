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
    UserShortListSerializer,
    UserListSerializer,
    UserCreateUpdateSerializer
)

from api.pagination import DefaultPageNumberPagination


class UserPaginatedView(ListAPIView):
    """
    get:
    Return a pagineted list of all the existing users.
    """

    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = UserListSerializer

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

# ViewSets define the view behavior.
class UserCreateView(CreateAPIView):
    """
    post:
    Create a new user instance.
    """

    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = UserCreateUpdateSerializer


class UserListView(APIView):
    """
    get:
    Return a list of all the existing users.

    post:
    Create a new user instance.
    """
    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = UserCreateUpdateSerializer(data=request.data)

        if serializer.is_valid():

            # A validação de email esta sendo realizada pelo model o qual
            # defini que o email é unico

            # dentro do .serializers até fiz um metodo para validate email
            # mas o fluxo do django não chega até ele pois realiza as
            # validações do model primeiro

            email = serializer.data.get('email')
            try:
                user = CustomUser(email=email)
                user.set_password(serializer.data.get('password'))
                user.save()

                Profile.objects.create(
                    user=user,
                    name=serializer.data.get('name')
                )

                # Adress
                # Não consegui realizar um post atraves de um DictField
                # e até mesmo atraves do AddressSerializer
                # por isso realizei manualmente o cadastro do modelo Address

                address_data = {
                    'street': serializer.data.get('street'),
                    'number': serializer.data.get('number'),
                    'district': serializer.data.get('district'),
                    'city': serializer.data.get('city'),
                    'state': serializer.data.get('state'),
                    'country': serializer.data.get('country')
                }

                Address.objects.create(user=user, **address_data)
            except Exception as e:

                return Response(
                    {
                        'errors': '{}'.format(e)
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # serializo a instancia do usuario criado

            user_created = UserListSerializer(user)
            return Response(
                user_created.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class UsersMeView(APIView):
    """
    get:
    Return existing users over token session.
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

        serializer = UserListSerializer(user)
        return Response(serializer.data)


class UserDetailCodeView(RetrieveAPIView):
    """
    get:
    Return the profile and user infos by code uuid.
    """

    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = UserListSerializer

    lookup_field = 'code'

    def get_queryset(self, *args, **kwargs):

        qs = CustomUser.objects.select_related('profile').all()

        return qs
