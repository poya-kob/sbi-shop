from django.contrib import admin

from .models import Blogs,Comments


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_editable = ['is_active']
    sortable_by = ['modified_date', 'is_active']
    list_display = ['__str__', 'is_active']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_editable = ['is_published']
    sortable_by = ['created', 'is_published']
    list_display = ['__str__', 'is_published']
