from django.urls import path

from .views import home, newsletter

urlpatterns = [
    path('', home, name='home'),
    path('newsletter/', newsletter, name='newsletter'),


]
