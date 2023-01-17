from django.urls import path

from .views import services_detail, services_list

urlpatterns = [
    path('service/', services_list, name='service_list'),
    path('service/<int:sid>/', services_detail, name='service_detail')
]
