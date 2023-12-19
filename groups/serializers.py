from rest_framework import serializers

from groups.models import Specialization, Semester, ClassField


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class SemesterSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer()

    class Meta:
        model = Semester
        fields = ['semester_id', 'number', 'specialization']


class ClassFieldSerializer(serializers.ModelSerializer):
    semester = SemesterSerializer()

    class Meta:
        model = ClassField
        fields = ['class_field_id', 'number', 'semester']
