from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Newsletter(models.Model):
    email = models.EmailField(unique=True, verbose_name=_('email'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('news letter')
        verbose_name_plural = _('news letter')
