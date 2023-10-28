from rest_framework import serializers

from groups.models import Specialization, Semester, ClassField


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'


class ClassFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassField
        fields = '__all__'
