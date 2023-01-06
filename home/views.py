import contextlib
from django.shortcuts import render, redirect

from blog.models import Blogs
from .models import Newsletter


def home(request):
    context = {
        'selected_blog': Blogs.objects.filter(selected_blog=True)[:2],
        'sliders': Blogs.objects.filter(show_on_slider=True)

    }
    return render(request, 'home/index.html', context)


def newsletter(request):
    with contextlib.suppress(Exception):
        Newsletter.objects.create(email=request.POST.get('email', None))
    return redirect(request.POST.get('next', '/'))
