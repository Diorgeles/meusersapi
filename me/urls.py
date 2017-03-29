# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

admin.autodiscover()

sitemaps = {
    # Place sitemaps here
}


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # SEO API's
    url(
        r'^sitemap\.xml$',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),

    url(
        r'^accounts/',
        include(
            'accounts.urls', namespace="accounts"
        )
    ),

    # API

    url(
        r'^api/v1/',
        include(
            'api.v1_urls', namespace="v1"
        )
    ),

    url(
        r'^api-token-auth/',
        obtain_jwt_token
    ),

    url(
        r'^api-token-refresh/',
        refresh_jwt_token
    ),

    url(
        r'^api-token-verify/',
        verify_jwt_token
    ),

    url(
        r'^api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    )



]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
