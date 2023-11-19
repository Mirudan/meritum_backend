from django.contrib import admin

from admins.models import Admin


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('login',)
    search_fields = ('login',)
