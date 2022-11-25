from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

from django_jalali.db import models as jmodels
from mptt import models as mp


class Categories(mp.MPTTModel):
    title = models.CharField(max_length=150)
    parent = mp.TreeForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['title']


class Blogs(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    body = RichTextUploadingField(verbose_name=_("body"))
    image = models.ImageField(verbose_name=_("image"))
    category = mp.TreeForeignKey(Categories, on_delete=models.SET_NULL, null=True, verbose_name=_('category'))
    video = models.FileField(verbose_name=_("video"))
    created_date = jmodels.jDateField(auto_now_add=True)
    modified_date = jmodels.jDateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
