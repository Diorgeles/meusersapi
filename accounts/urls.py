# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports

# Core Django imports
from django.conf.urls import url
# Third-party app imports

# Imports from your apps
from .views import (
    UserListView,
    UserPaginatedView,
    UserCreateView,
    UsersMeView,
    UserDetailCodeView
)

from .views_profile import (
    ProfileMeView,
    ProfileDetailCodeView
)

urlpatterns = [
    url(
        r'^$',
        UserListView.as_view(),
        name='list-and-create'
    ),
    url(
        r'^paginated/$',
        UserPaginatedView.as_view(),
        name='paginated'
    ),
    url(
        r'^me/$',
        UsersMeView.as_view(),
        name='me'
    ),
    url(
        r'^me/profile/$',
        ProfileMeView.as_view(),
        name='me-profile'
    ),
    url(
        r'^profile/(?P<code>[0-9a-z-]+)/$',
        ProfileDetailCodeView.as_view(),
        name='profile-code'
    ),
    url(
        r'^(?P<code>[0-9a-z-]+)/$',
        UserDetailCodeView.as_view(),
        name='user-detail-code'
    ),
    url(
        r'^(?P<code>[0-9a-z-]+)/profile/$',
        UserDetailCodeView.as_view(),
        name='user-detail-code-profile'
    ),

]
