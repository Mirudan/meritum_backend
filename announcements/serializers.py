from rest_framework import serializers

from announcements.models import News, Course
from teachers.serializers import TeacherSerializer


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()

    class Meta:
        model = Course
        fields = ['course_id', 'title', 'content', 'image', 'publication_date', 'teacher']
