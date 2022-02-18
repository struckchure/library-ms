from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from accounts.forms import UserLoginForm, UserRegisterForm
from library.models import Borrow


@login_required
def user_dashboard_view(request):
    borrowed_books = Borrow.objects.filter(user=request.user)
    context = {"user": request.user, "borrowed_books": borrowed_books}

    return render(request, "accounts/dashboard.html", context)


def user_registration_view(request):
    if request.method == "POST":
        registration_form = UserRegisterForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
        else:
            messages.error(request, registration_form.errors)

            return redirect("accounts:register")
    else:
        registration_form = UserRegisterForm()

    context = {"registration_form": registration_form}

    return render(request, "accounts/register.html", context)


def user_login_view(request):
    if request.method == "POST":
        login_form = UserLoginForm(request, request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            login(request, user)

            next_url = request.GET.get("next")
            if next_url:
                return redirect(next_url)

            return redirect("accounts:dashboard")
        else:
            messages.error(request, login_form.errors)

            return redirect("accounts:login")
    else:
        login_form = UserLoginForm()

    context = {"login_form": login_form}

    return render(request, "accounts/login.html", context)


def user_logout_view(request):
    logout(request)

    return redirect("accounts:dashboard")
