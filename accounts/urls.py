from django.urls import path

from accounts.views import user_registration_view

app_name = "accounts"

urlpatterns = [path("register/", user_registration_view, name="register")]
