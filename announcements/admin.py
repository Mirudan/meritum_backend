from django.contrib import admin

from announcements.models import News, Course


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('publication_date',)
    search_fields = ('title',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher')
    list_filter = ('publication_date',)
    search_fields = ('title', 'teacher')
