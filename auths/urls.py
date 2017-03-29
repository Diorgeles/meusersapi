# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports

# Core Django imports
from django.conf.urls import url, include
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

# Third-party app imports

# Imports from your apps
from .views import LoginView
from django.contrib.auth.views import logout_then_login

urlpatterns = [
]
