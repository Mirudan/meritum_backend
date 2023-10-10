from rest_framework import serializers

from announcements.models import News, Course


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
