from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = "account"

urlpatterns = [
    path("register", views.register_view, name="register_view"),
    # path("login", obtain_auth_token, name="login_view")
    path("login", views.login_view, name="login_view")
]
