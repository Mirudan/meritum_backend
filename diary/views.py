from django.shortcuts import render
from rest_framework import generics
from admins.permissions import IsAdminUser
from diary.models import Schedule
from diary.serializers import ScheduleSerializer, ScheduleSerializerCreate
from rest_framework.permissions import AllowAny


class ScheduleAPIList(generics.ListAPIView):
    """
    Показывает весь список новостей по GET запросу
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleAPIListCreate(generics.ListCreateAPIView):
    """
    Показывает весь список новостей по GET запросу и дает возможность внесения данных
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializerCreate
    # permission_classes = [AllowAny, IsAdminUser]


class ScheduleAPIRUDV(generics.RetrieveUpdateDestroyAPIView):
    """
    Отображение конкретных данных с возможностью внесения, изменения и удаления
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    # permission_classes = [AllowAny, IsAdminUser]
