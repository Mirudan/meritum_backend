from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentObtainTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()