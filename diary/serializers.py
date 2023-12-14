from rest_framework import serializers

from diary.models import Subject, Mark, Schedule, PlanLesson
from groups.serializers import ClassFieldSerializer, SpecializationSerializer
from students.serializers import StudentSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subjects_id', 'name']


class PlanLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanLesson
        fields = '__all__'


class MarkSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Mark
        fields = ['date_mark', 'mark_id', 'mark', 'student', 'subject']


class MarkSerializerCreate(serializers.ModelSerializer):
    # костыльный сериализатор
    class Meta:
        model = Mark
        fields = ['date_mark', 'mark_id', 'mark', 'student', 'subject']


class ScheduleSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    class_field = ClassFieldSerializer(read_only=True)
    specialization = SpecializationSerializer(read_only=True)
    plan_lesson = PlanLessonSerializer(read_only=True)

    class Meta:
        model = Schedule
        fields = ['schedule_id', 'specialization', 'subject', 'class_field', 'date_lesson', 'plan_lesson']


class ScheduleSerializerCreate(serializers.ModelSerializer):
    # костыльный сериализатор
    class Meta:
        model = Schedule
        fields = ['schedule_id', 'specialization', 'subject', 'class_field', 'date_lesson', 'plan_lesson']
