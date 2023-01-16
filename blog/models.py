from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

from django_jalali.db import models as jmodels
from mptt import models as mp

from categories.models import Categories
from .mangers import BlogsManager, CommentManager
from utils import upload_image_path, upload_video_path


class Blogs(models.Model):
    title = models.CharField(_("title"), max_length=200, )
    body = RichTextUploadingField(verbose_name=_("body"))
    image = models.ImageField(verbose_name=_("image"), upload_to=upload_image_path)
    category = mp.TreeForeignKey(Categories, on_delete=models.SET_NULL, null=True, related_name='blogs',
                                 verbose_name=_('category'))
    video = models.FileField(verbose_name=_("video"), upload_to=upload_video_path, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_('user'))
    created_date = jmodels.jDateField(auto_now_add=True)
    modified_date = jmodels.jDateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False, verbose_name=_('is active'))
    show_on_slider = models.BooleanField(default=False, verbose_name=_('show on slider'))
    selected_blog = models.BooleanField(default=False, verbose_name=_('selected blog'))
    objects = BlogsManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')


class Comments(mp.MPTTModel):
    first_name = models.CharField(max_length=150, null=True, blank=True, verbose_name=_('first name'))
    last_name = models.CharField(max_length=150, null=True, blank=True, verbose_name=_('last name'))
    email = models.EmailField(verbose_name=_('email'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='comments',
                             verbose_name=_('user'))
    title = models.CharField(max_length=200, null=True, verbose_name=_('title'))
    body = models.TextField(verbose_name=_('body'))
    created = jmodels.jDateField(auto_now_add=True)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='comments', verbose_name=_('blog'))
    parent = mp.TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                               verbose_name=_('parent'))
    is_published = models.BooleanField(default=False, verbose_name=_('is active'))

    objects = CommentManager()

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
