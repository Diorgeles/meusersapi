# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports

# Core Django imports
from django.http import Http404

# Third-party app imports

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.reverse import reverse
# Imports from your apps



class APIRoot(APIView):

    def get(self, request, format=None):

        data = {
            'usuarios': reverse(
                'users:list-and-create',
                request=request
            )
        }
        return Response(data)
