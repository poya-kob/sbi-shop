from django.db import models

from django_jalali.db import models as jmodels
from mptt import models as mp


class Categories(mp.MPTTModel):
    title = models.CharField(max_length=150)
    parent = mp.TreeForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)
    created_time = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['title']
