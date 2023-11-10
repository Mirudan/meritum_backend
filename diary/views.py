from django.shortcuts import render
from rest_framework import generics
from admins.permissions import IsAdminUser
from diary.models import Schedule, Mark
from diary.serializers import ScheduleSerializer, ScheduleSerializerCreate, MarkSerializer, MarkSerializerCreate
from rest_framework.permissions import AllowAny


class ScheduleAPIList(generics.ListAPIView):
    """
    Показывает все расписание по GET запросу
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleAPIListCreate(generics.ListCreateAPIView):
    """
    Показывает все расписание по GET запросу и дает возможность внесения данных
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


class MarkAPIList(generics.ListAPIView):
    """
    Показывает весь список оценок по GET запросу
    """
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


class MarkAPIListCreate(generics.ListCreateAPIView):
    """
    Показывает все оценки по GET запросу и есть возможность внесения данных
    """
    queryset = Mark.objects.all()
    serializer_class = MarkSerializerCreate
