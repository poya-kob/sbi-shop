from django.db import models

from django_jalali.db import models as jmodels


class ContactUs(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    text = models.TextField()
    date = jmodels.jDateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __init__(self):
        super().__init__()
        self.is_read = True
        self.save()
