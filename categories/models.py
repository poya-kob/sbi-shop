from django.db import models
from django.utils.translation import gettext_lazy as _

from django_jalali.db import models as jmodels
from mptt import models as mp


class Categories(mp.MPTTModel):
    title = models.CharField(max_length=150,verbose_name=_('title'))
    parent = mp.TreeForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True,verbose_name=_('parent'))
    created_time = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['created_time', 'title']
