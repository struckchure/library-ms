from django import forms
from django.contrib.auth.forms import UserCreationForm
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
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
