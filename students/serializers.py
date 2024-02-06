from djoser.serializers import UserSerializer
from rest_framework import serializers

from groups.serializers import ClassFieldSerializer, SpecializationSerializer
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class_field = ClassFieldSerializer()
    user = UserSerializer()
    specialization = SpecializationSerializer()

    class Meta:
        model = Student
        fields = '__all__'