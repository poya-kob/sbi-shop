from django.db.models import Manager, Q
from mptt.models import TreeManager


class BlogsManager(Manager):
    def get_active_blogs(self):
        return self.get_queryset().filter(is_active=True)

    def get_last_post(self):
        return self.get_active_blogs().order_by('-id')[:3]

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(category__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, is_active=True).distinct()


class CommentManager(TreeManager):
    def get_active_comments(self):
        return self.get_queryset().filter(is_published=True)
