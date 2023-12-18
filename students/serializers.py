from rest_framework import serializers

from groups.serializers import ClassFieldSerializer
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class_field = ClassFieldSerializer()

    class Meta:
        model = Student
        fields = '__all__'
