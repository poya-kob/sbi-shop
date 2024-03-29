
from django.core import serializers
from django.shortcuts import redirect, resolve_url
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, View
from .models import Blogs, Comments
from .forms import CommentsForm


class BlogList(ListView):
    template_name = 'blog/blog_list.html'
    paginate_by = 1
    queryset = Blogs.objects.get_active_blogs().order_by("modified_date")
    context_object_name = 'blogs'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        categories = {blog.category for blog in self.queryset}
        context['categories'] = categories
        context['posts'] = Blogs.objects.get_last_post()
        return context

    def get_queryset(self):
        query = super().get_queryset()
        if self.request.GET.get('cat', False):
            query = query.filter(category_id=int(self.request.GET.get('cat')))
        return query


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
        if request.POST.get('comment_id'):
            comment = Comments.objects.create(user_id=request.user.id,
                                              body=request.POST.get('comment_text'),
                                              parent_id=request.POST.get('comment_id'), blog_id=pk,
                                              is_published=True)
            response_data = serializers.serialize('json', [comment, request.user])

            return JsonResponse(response_data, safe=False)
        comment = CommentsForm(request.POST)

        if comment.is_valid():
            if request.user.is_authenticated:
                Comments.objects.create(user_id=request.user.id, **comment.cleaned_data)
            else:
                Comments.objects.create(**comment.cleaned_data)
        return redirect(resolve_url('blog_detail', pk=pk))


class Search(ListView):
    model = Blogs
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 10

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        return Blogs.objects.search(query)
