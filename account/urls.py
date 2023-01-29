from django.urls import path

from .views import LogoutPage

urlpatterns = [
    path("logout-user/", LogoutPage.as_view(), name="logout_user")
]
