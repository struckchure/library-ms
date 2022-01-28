from django.urls import path

from accounts.views import (
    user_dashboard_view,
    user_login_view,
    user_logout_view,
    user_registration_view,
)

app_name = "accounts"

urlpatterns = [
    path("accounts/", user_dashboard_view, name="dashboard"),
    path("accounts/register/", user_registration_view, name="register"),
    path("accounts/login/", user_login_view, name="login"),
    path("accounts/logout/", user_logout_view, name="logout"),
]
