from django.shortcuts import render
from rest_framework import generics

from groups.models import Specialization
from groups.serializers import SpecializationSerializer


# Create your views here.
class SpecializationAPIList(generics.ListAPIView):
    """
    Показывает весь список специальностей
    """
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
