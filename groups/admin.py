from django.contrib import admin

from groups.models import Specialization, Semester, ClassField


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('specialization_id', 'name')
    list_filter = ('specialization_id', 'name')
    search_fields = ('specialization_id', 'name')


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('number', )
    list_filter = ('number', )
    search_fields = ('number', )


@admin.register(ClassField)
class ClassFieldAdmin(admin.ModelAdmin):
    list_display = ('number',)
    list_filter = ('number',)
    search_fields = ('number',)
