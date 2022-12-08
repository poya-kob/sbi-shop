from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

from django_jalali.db import models as jmodels
from mptt import models as mp

from categories.models import Categories
from .mangers import BlogsManager
from utils import upload_image_path


class Blogs(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    body = RichTextUploadingField(verbose_name=_("body"))
    image = models.ImageField(verbose_name=_("image"), upload_to=upload_image_path)
    category = mp.TreeForeignKey(Categories, on_delete=models.SET_NULL, null=True, related_name='blogs',
                                 verbose_name=_('category'))
    video = models.FileField(verbose_name=_("video"), null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date = jmodels.jDateField(auto_now_add=True)
    modified_date = jmodels.jDateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    objects = BlogsManager()

    def __str__(self):
        return self.title


class Comments(mp.MPTTModel):
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='comments')
    parent = mp.TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
