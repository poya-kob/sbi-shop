from django.shortcuts import render
from django.views.generic import ListView
from .models import Blogs


class BlogList(ListView):
    template_name = 'blog/blog_list.html'
    paginate_by = 5
    queryset = Blogs.objects.filter(is_active=True).order_by("modified_date")
    context_object_name = 'blogs'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        categories = {blog.category for blog in self.queryset}
        context['categories'] = categories
        return context
