from django.db import models

from django_jalali.db import models as jmodels


class ContactUs(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=250)
    email = models.EmailField()
    text = models.TextField()
    date = jmodels.jDateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

