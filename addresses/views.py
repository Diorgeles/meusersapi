# -*- coding:utf-8 -*-
from __future__ import unicode_literals

# Stdlib imports

# Core Django imports
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _

# Third-party app imports

# Imports from your apps
