# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext as _

# Relative imports of the 'app-name' package


class CustomUserQueryset(models.query.QuerySet):
    """
    Classe para definir os querysets
    """
    pass


class CustomUserManager(BaseUserManager, models.Manager):
    """
    Define um manager para o model de usuarios
    """
    def get_queryset(self):
        return CustomUserQueryset(self.model, using=self._db)

    def create_user(
        self,
        email,
        password=None,
        **extra_fields
    ):
        """
        Cria e salva um usuário com o email passado e senha
        """
        if not email:
            raise ValueError(_(u'Usuários devem possuir um email'))

        user = self.model(
            email=CustomUserManager.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self,
        email,
        password=None,
        **extra_fields
    ):
        """
        Cria e salva um super-usuário com o email passado e senha
        """

        user = self.create_user(
            email,
            password,
            **extra_fields
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
