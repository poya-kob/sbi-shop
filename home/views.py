from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from blog.models import Blogs
from gallery.models import Gallery
from service.models import Services
from .models import Newsletter
from utils import grouper


def home(request):
    gallery = Gallery.objects.filter(is_active=True).order_by('-created')
    grouped_gallery = list(grouper(gallery, 5))
    context = {
        'selected_blog': Blogs.objects.filter(selected_blog=True).order_by('-modified_date')[:2],
        'sliders': Blogs.objects.filter(show_on_slider=True),
        'last_blogs': Blogs.objects.get_active_blogs().order_by('modified_date')[:5],
        'selected_services': Services.objects.filter(selected_service=True, is_active=True)[:4],
        'grouped_gallery': grouped_gallery

    }
    return render(request, 'home/index.html', context)


def newsletter(request):
    try:
        Newsletter.objects.create(email=request.POST.get('email', None))
        messages.success(request, _('email submitted successfully.'))
    except Exception as error:
        messages.error(request, _('submit email failed.'))

    return redirect(request.POST.get('next', '/'))


