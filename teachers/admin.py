from django.contrib import admin

from teachers.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subjects')
    list_filter = ('full_name', 'subjects')
    search_fields = ('full_name', 'subjects')
