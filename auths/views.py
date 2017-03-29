# -*- coding:utf-8 -*-
from __future__ import unicode_literals

# Stdlib imports

# Core Django imports
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Third-party app imports

# Imports from your apps
from .forms import LoginForm
