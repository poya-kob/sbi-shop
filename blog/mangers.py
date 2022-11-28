from django.db.models import Manager


class BlogsManager(Manager):
    def get_active_blogs(self):
        return self.get_queryset().filter(is_active=True)
