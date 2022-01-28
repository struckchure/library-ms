from django.shortcuts import render
from django.contrib import messages

from accounts.forms import UserRegisterForm


def user_registration_view(request):
    if request.method == "POST":
        registration_form = UserRegisterForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
        else:
            messages.error(registration_form.error_messages)
    else:
        registration_form = UserRegisterForm()

    context = {"registration_form": registration_form}

    return render(request, "accounts/register.html", context)
