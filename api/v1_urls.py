
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports

# Core Django imports
from django.conf.urls import url

# Third-party app imports
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
# Imports from your apps


from .v1_api import APIRoot


# http -a admin:password123 http://127.0.0.1:8000/users/

# router = DefaultRouter()
# router.register(r'scheduling', SchedulingsViewSet, 'Scheduling')
# urlpatterns = router.urls


urlpatterns = [
    url(
        r'^$',
        APIRoot.as_view(),
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
