from django.urls import path

from .views import home, newsletter, services_list, services_detail

urlpatterns = [
    path('', home, name='home'),
    path('newsletter/', newsletter, name='newsletter'),
    path('service/', services_list, name='service_list'),
    path('service/<int:sid>/', services_detail, name='service_detail')

]
