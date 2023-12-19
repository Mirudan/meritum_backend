from rest_framework import serializers

from groups.models import Specialization, ClassField


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class ClassFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassField
        fields = ['class_field_id', 'number']
