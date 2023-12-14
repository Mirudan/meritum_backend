from rest_framework import serializers

from groups.serializers import ClassFieldSerializer
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class_field = ClassFieldSerializer()

    class Meta:
        model = Student
        fields = ['student_id', 'full_name', 'login', 'password', 'email', 'class_field']


class StudentObtainTokenSerializer(serializers.Serializer):
    class Meta:
        model = Student
        fields = ('email', 'password')
