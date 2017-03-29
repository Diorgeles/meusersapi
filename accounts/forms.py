# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports


# Core Django imports

from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    SetPasswordForm,
    PasswordChangeForm,
    ReadOnlyPasswordHashField
)
from django.contrib.auth.models import Group
from django.forms.formsets import formset_factory

# Third-party app imports

# from allauth.account.forms import UserForm, PasswordField, SetPasswordField
# from allauth.account.adapter import get_adapter
# Realative imports of the 'app-name' package
from .models import CustomUser, Profile


# usado no admin
class CustomUserCreationForm(UserCreationForm):

    class Meta:

        model = CustomUser

        fields = '__all__'

        exclude = ('is_staff',)


# usado no admin
class CustomUserChangeForm(UserChangeForm):

    class Meta:

        model = CustomUser

        fields = '__all__'


class UserProfileEditForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = '__all__'

        exclude = ['user']

        help_texts = {
            'name': _(
                _(u'Exemplo: João Ricardo')
            ),
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira o primeiro nome'),
                }
            ),
        }


# usado em views
class UserProfileForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = '__all__'

        exclude = ['user']

        help_texts = {
            'name': _(
                _(u'Exemplo: João Ricardo')
            ),
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira o primeiro nome'),
                }
            ),
        }


class CustomUserForm(UserCreationForm):

    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
        help_text=_("Enter the same password as above, for verification.")
    )

    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()
            user.groups = self.cleaned_data['groups']
            user.save()

        return user

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'is_staff', 'groups']

        help_texts = {
            'email': _(
                _(u'Exemplo: email@domain.com')
            ),
        }

        widgets = {
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira um email válido'),
                }
            ),
            'groups': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            )

        }


UserFormSet = formset_factory(CustomUserForm, extra=0, max_num=0)


class CustomUserEditForm(UserChangeForm):

    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Não são armazenadas senhas no formato plano, "
            "por isso não há como visualizar a senha do usuário, "
            "mas você pode alterá-la usando "
            "<a href='password'>este formulário</a>."
        )
    )

    def save(self, commit=True):

        user = super(CustomUserEditForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password']
        user.groups = self.cleaned_data['groups']

        if commit:
            user.save()
        return user

    class Meta:
        fields = ['password', 'email', 'is_staff', 'groups']
        model = CustomUser

        help_texts = {
            'email': _(
                _(u'Exemplo: email@domain.com')
            ),
        }

        widgets = {
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _(u'Insira um email válido'),
                }
            ),
            'groups': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            )

        }


class UserPasswordChangeEditForm(SetPasswordForm):

    new_password1 = forms.CharField(
        label=_("Nova senha"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    new_password2 = forms.CharField(
        label=_("Repita a nova senha"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
        help_text=_("Enter the same password as above, for verification.")
    )

    class Meta:

        model = CustomUser


class ProfilePasswordChangeEditForm(PasswordChangeForm):

    old_password = forms.CharField(
        label=_("Senha antiga"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    new_password1 = forms.CharField(
        label=_("Nova senha"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    new_password2 = forms.CharField(
        label=_("Repita a nova senha"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
        help_text=_("Enter the same password as above, for verification.")
    )

    class Meta:

        model = CustomUser


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'

        help_texts = {
            'permissions': _(
                _(u'Pressione CTRL para selecionar mais de uma permissão')
            ),
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'permissions': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            )
        }
