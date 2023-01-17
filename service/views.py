from django.shortcuts import render, redirect, reverse

from .models import Services
from utils import grouper


def services_list(request):
    services = Services.objects.filter(is_active=True)
    grouped_services = list(grouper(services, 3))
    context = {
        'grouped_services': grouped_services,
        'title': 'لیست خدمات'
    }
    return render(request, 'home/service_list.html', context)


def services_detail(request, sid: int):
    context = {
        'service': Services.objects.get(id=sid, is_active=True),
        'title': 'جزییات خدمت'

    }
    if context['service']:
        return render(request, 'home/service_detail.html', context)
    else:
        return redirect(reverse('service_list'))
