from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

from django_jalali.db import models as jmodels

from utils import upload_image_path, upload_video_path


class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    body = RichTextUploadingField(verbose_name=_("body"))
    image = models.ImageField(verbose_name=_("image"), upload_to=upload_image_path)
    video = models.FileField(verbose_name=_("video"), upload_to=upload_video_path, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date = jmodels.jDateField(auto_now_add=True)
    modified_date = jmodels.jDateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    selected_service = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
