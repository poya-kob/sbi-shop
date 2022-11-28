from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blogs


class BlogList(ListView):
    template_name = 'blog/blog_list.html'
    paginate_by = 5
    queryset = Blogs.objects.get_active_blogs().order_by("modified_date")
    context_object_name = 'blogs'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        categories = {blog.category for blog in self.queryset}
        context['categories'] = categories
        return context


class BlogDetail(DetailView):
    template_name = 'blog/blog_detail.html'
    queryset = Blogs.objects.get_active_blogs()
    context_object_name = 'blog'
