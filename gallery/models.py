from django.db import models
from django.utils.translation import gettext_lazy as _

from utils import upload_image_path


class Gallery(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    image = models.ImageField(upload_to=upload_image_path, verbose_name=_('image'))
    created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False, verbose_name=_('is active'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('gallery')
