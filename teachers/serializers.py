from rest_framework import serializers

from teachers.models import Teacher


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'