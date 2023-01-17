from django.contrib import admin

from .models import Services


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_editable = ['is_active']
    list_display = ['__str__', 'is_active']
    readonly_fields = ['user']

    def save_model(self, request, obj, form, change):
        if obj.user is None:
            obj.user = request.user

        super().save_model(request, obj, form, change)
