from rest_framework import serializers
from .models import Admin


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class AdminObtainTokenSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField()