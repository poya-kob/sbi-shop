from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from blog.models import Blogs
from gallery.models import Gallery
from .models import Newsletter, Services
from utils import grouper


def home(request):
    gallery = Gallery.objects.filter(is_active=True).order_by('-created')
    grouped_gallery = list(grouper(gallery, 5))
    context = {
        'selected_blog': Blogs.objects.filter(selected_blog=True)[:2],
        'sliders': Blogs.objects.filter(show_on_slider=True),
        'last_blogs': Blogs.objects.get_active_blogs().order_by('modified_date')[:5],
        'selected_services': Services.objects.filter(selected_service=True, is_active=True)[:4],
        'grouped_gallery': grouped_gallery

    }
    return render(request, 'home/index.html', context)


def newsletter(request):
    try:
        Newsletter.objects.create(email=request.POST.get('email', None))
        messages.success(request, 'email submitted successfully.')
    except Exception as error:
        messages.error(request, 'submit email failed.')

    return redirect(request.POST.get('next', '/'))


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
