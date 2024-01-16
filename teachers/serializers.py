from rest_framework import serializers
from djoser.serializers import UserSerializer

from teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Teacher
        fields = '__all__'