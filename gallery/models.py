from django.db import models

from utils import upload_image_path


class Gallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_image_path)
    created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

