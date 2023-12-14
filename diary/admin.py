from django.contrib import admin

from diary.models import Subject, Mark, Schedule


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subjects_id', 'name')
    list_filter = ('subjects_id', 'name')
    search_fields = ('subjects_id', 'name')


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('mark', 'student', 'subject', 'date_mark')
    list_filter = ('mark', 'student', 'subject', 'date_mark')
    search_fields = ('mark', 'student', 'subject', 'date_mark')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date_lesson')
    list_filter = ('subject', 'date_lesson')
    search_fields = ('subject', 'date_lesson')
