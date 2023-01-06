from django.shortcuts import render, redirect
from django.contrib import messages

from blog.models import Blogs
from .models import Newsletter


def home(request):
    context = {
        'selected_blog': Blogs.objects.filter(selected_blog=True)[:2],
        'sliders': Blogs.objects.filter(show_on_slider=True)

    }
    return render(request, 'home/index.html', context)


def newsletter(request):
    try:
        Newsletter.objects.create(email=request.POST.get('email', None))
        messages.success(request, 'email submitted successfully.')
    except Exception as error:
        messages.error(request, 'submit email failed.')

    return redirect(request.POST.get('next', '/'))
