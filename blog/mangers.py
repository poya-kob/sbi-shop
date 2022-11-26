from django.db.models import Manager


class BlogsManager(Manager):
    def get_active_blogs(self):
        self.get_queryset().filter(is_active=True)
