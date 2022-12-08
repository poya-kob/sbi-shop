from django.shortcuts import redirect, resolve_url
from django.views.generic import ListView, DetailView, View
from .models import Blogs, Comments
from .forms import CommentsForm


class BlogList(ListView):
    template_name = 'blog/blog_list.html'
    paginate_by = 5
    queryset = Blogs.objects.get_active_blogs().order_by("modified_date")
    context_object_name = 'blogs'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        categories = {blog.category for blog in self.queryset}
        context['categories'] = categories
        context['posts'] = Blogs.objects.get_last_post()
        return context


class BlogDetail(DetailView):
    template_name = 'blog/blog_detail.html'
    queryset = Blogs.objects.get_active_blogs()
    context_object_name = 'blog'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        categories = {blog.category for blog in self.queryset}
        context['categories'] = categories
        context['posts'] = Blogs.objects.get_last_post()
        context['comment'] = CommentsForm(initial={'id_blog': kwargs['object'].id})

        return context


class CommentsView(View):
    def post(self, request, pk):
        comment = CommentsForm(request.POST)

        if comment.is_valid():
            if request.user.is_authenticated:
                Comments.objects.create(user_id=request.user.id, **comment.cleaned_data)
            else:
                Comments.objects.create(**comment.cleaned_data)
        return redirect(resolve_url('blog_detail', pk=pk))
