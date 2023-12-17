from django.contrib import admin

from groups.models import Specialization, Semester, ClassField


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('specialization_id', 'name')
    list_filter = ('specialization_id', 'name')
    search_fields = ('specialization_id', 'name')


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('number', 'specialization')
    list_filter = ('number', 'specialization')
    search_fields = ('number', 'specialization')


@admin.register(ClassField)
class ClassFieldAdmin(admin.ModelAdmin):
    list_display = ('number', 'semester')
    list_filter = ('number', 'semester')
    search_fields = ('number', 'semester')
