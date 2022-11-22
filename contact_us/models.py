from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    text = models.TextField()
    is_read = models.BooleanField(default=False)

    def __init__(self):
        super().__init__()
        self.is_read = True
        self.save()

