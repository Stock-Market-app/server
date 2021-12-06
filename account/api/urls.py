from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = "account"

urlpatterns = [
    path("checklogin", views.index, name="check_login"),
    path("register", views.register_view, name="register_view"),
    # path("login", obtain_auth_token, name="login_view")
    path("login", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout_view"),
    path("watchlist", views.watchlist, name="watchlist_view")
]
