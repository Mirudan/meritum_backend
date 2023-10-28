from rest_framework import serializers

from diary.models import Subject, Mark, Schedule
from groups.serializers import ClassFieldSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    class_field = ClassFieldSerializer()

    class Meta:
        model = Schedule
        fields = ['schedule_id', 'date_lesson', 'start_time', 'finish_time', 'subject', 'class_field']
