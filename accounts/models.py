# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports
import uuid
# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_delete
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
# Third-party app imports
from django_extensions.db.models import (
    TimeStampedModel
)
from rest_framework.authtoken.models import Token
# Imports from your apps

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """
    Modelo para salvar o usuario somente com o email
    """
    code = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    email = models.EmailField(
        _('email address'), max_length=255,
        unique=True, db_index=True
    )

    is_staff = models.BooleanField(
        _('staff status'), default=False, help_text=_(
            'Designates whether the user can log into this admin site.'
        )
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as '
            'active. Unselect this instead of deleting accounts.'
        )
    )

    date_joined = models.DateTimeField(
        _('date joined'),
        default=timezone.now
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    is_admin = models.BooleanField(
        verbose_name=_(u'Administrador'),
        default=False,
        help_text=_(u'Designa este usuário como administrador.')
    )

    objects = CustomUserManager()

    def get_full_name(self):
        """
        Retorna o primeiro nome mais o ultimo nome, com
        um espaço entre eles
        """
        full_name = u'{}'.format(
            self.get_profile().get_full_name()
        )
        return full_name.strip()

    full_name = property(get_full_name)

    def get_short_name(self):
        """
        Retorna somente o primeiro nome
        """
        try:
            return u'{}'.format(self.get_profile().first_name)
        except Exception as e:
            return '{} '.format(
                self.email,
            )

    def get_profile(self):
        """
        Alias para buscar o perfil do usuario
        """

        try:
            return self.userprofile
        except Exception as e:
            return None

    def __str__(self):

        try:
            return self.get_full_name()
        except Exception as e:
            return '{} '.format(
                self.email,
            )

    class Meta:

        verbose_name = _(u'Usuário')
        verbose_name_plural = _(u'Usuários')

        permissions = (
            (
                'can_access_users',
                'Acesso aos usuarios'
            ),
        )


class Profile(TimeStampedModel):
    """
    Perfil do usuario
    """

    user = models.OneToOneField(
        CustomUser,
        verbose_name=_('Usuário')
    )

    code = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    name = models.CharField(
        max_length=255,
        verbose_name=_(u'Nome completo'),
        blank=True,
        null=True
    )

    def get_full_name(self):
        """
        Retorna o nome completo do cliente
        """
        return u'{}'.format(
            self.name,
        )

    def __unicode__(self):

        user = '{}'.format(
            self.user.email,
        )

        return user

    __str__ = __unicode__

    class Meta:

        verbose_name = _(u'Perfil')
        verbose_name_plural = _(u'Perfis')

        permissions = (
            ('can_access_administration', 'Acesso aos menus de administração'),
            ('can_access_user', 'Acesso aos menus de usuários'),
            ('can_change_own_password', 'Alterar a propria senha'),
            ('can_access_group', 'Acesso aos menus de grupos de usuários'),
        )


def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


def delete_user_profile(sender, instance, using, **kwargs):
    if not using:
        Profile.objects.get(user=instance).delete()


# post_save.connect(create_user_profile, sender=CustomUser)
post_save.connect(create_auth_token, sender=CustomUser)
pre_delete.connect(delete_user_profile, sender=CustomUser)
