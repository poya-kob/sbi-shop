from django.db import models
from django.utils.translation import gettext_lazy as _

from django_jalali.db import models as jmodels


class ContactUs(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('first name'))
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('last name'))
    title = models.CharField(max_length=250, verbose_name=_('title'))
    email = models.EmailField(verbose_name=_('email'))
    text = models.TextField(verbose_name=_('body'))
    date = jmodels.jDateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, verbose_name=_('is read'))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('contact us')
        verbose_name_plural = _('contact us')
