# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports

# Core Django imports

# Third-party app imports
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)
from rest_framework.response import Response
# Imports from your apps


class DefaultLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class DefaultPageNumberPagination(PageNumberPagination):
    page_size = 1

    def get_paginated_response(self, data):

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'pagination': {
                'current_page': self.page.number,
                'total_pages': self.page.paginator.num_pages,
                'total_items': self.page.paginator.count,
            },
            'results': data
        })
