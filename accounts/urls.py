# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports

# Core Django imports
from django.conf.urls import url
# Third-party app imports

# Imports from your apps
from .views import (
    UserListView
)

urlpatterns = [
    url(
        r'^$',
        UserListView.as_view(),
        name='users-list'
    ),
]
