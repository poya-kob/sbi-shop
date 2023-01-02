from django.shortcuts import render

from blog.models import Blogs


def home(request):
    context = {
        'selected_blog': Blogs.objects.filter(selected_blog=True)[:2],
        'sliders': Blogs.objects.filter(show_on_slider=True)

    }
    return render(request, 'home/index.html', context)
