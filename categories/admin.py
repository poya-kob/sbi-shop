from django.contrib import admin
from .models import Categories


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    pass
