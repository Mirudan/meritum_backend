from django.contrib import admin

from groups.models import Specialization, ClassField


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('specialization_id', 'name')
    list_filter = ('specialization_id', 'name')
    search_fields = ('specialization_id', 'name')


@admin.register(ClassField)
class ClassFieldAdmin(admin.ModelAdmin):
    list_display = ('number',)
    list_filter = ('number',)
    search_fields = ('number',)
