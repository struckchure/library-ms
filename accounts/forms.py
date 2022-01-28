from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]
        labels = {
            "username": _("Username"),
            "email": _("E-Mail"),
        }


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
