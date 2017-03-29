# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports
# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _
# Third-party app imports
from django_extensions.db.models import (
    TimeStampedModel
)
# Imports from your apps


class Address(TimeStampedModel):
    """
    Endereços do usuário
    """

    user = models.ForeignKey(
        'accounts.CustomUser',
        verbose_name=_('Usuário'),
        related_name='address'
    )

    street = models.CharField(
        verbose_name=_(u'Endereço'),
        max_length=255
    )

    number = models.CharField(
        verbose_name=_(u'Número'),
        max_length=10
    )

    district = models.CharField(
        verbose_name=_(u'Bairro'),
        max_length=255
    )

    city = models.CharField(
        verbose_name=_(u'Cidade'),
        max_length=255
    )

    state = models.CharField(
        verbose_name=_(u'Estado'),
        max_length=255
    )

    country = models.CharField(
        verbose_name=_(u'País'),
        max_length=255
    )

    def __unicode__(self):
        return u'{},{},{} - {}, {}, {}'.format(
            self.street,
            self.number,
            self.district,
            self.city,
            self.state,
            self.country
        )

    __str__ = __unicode__

    class Meta:

        verbose_name = _(u'Endereço')
        verbose_name_plural = _(u'Endereços')
