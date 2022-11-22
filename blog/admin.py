from django.contrib import admin

from .models import Blogs


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_editable = ['is_active']
    sortable_by = ['modified_date', 'is_active']
    list_display = ['__str__', 'is_active']
