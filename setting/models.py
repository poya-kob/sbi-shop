from django.db import models
from django.utils.translation import gettext_lazy as _

from utils import upload_image_path


class SiteSetting(models.Model):
    site_title = models.CharField(max_length=200, verbose_name=_("site title"))
    telephone = models.CharField(max_length=12, verbose_name=_("telephone"), null=True, blank=True)
    mobile = models.CharField(max_length=12, verbose_name=_("mobile"))
    address = models.TextField(verbose_name=_("address"), null=True, blank=True)
    logo = models.ImageField(upload_to=upload_image_path, verbose_name=_("logo"))
    email = models.EmailField(verbose_name=_("email"))
    instagram_id = models.CharField(max_length=50, verbose_name=_("instagram id"), null=True, blank=True)
    telegram_id = models.CharField(max_length=50, verbose_name=_("telegram id"), null=True, blank=True)

    def __str__(self):
        return self.site_title
