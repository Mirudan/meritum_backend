from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Teacher
from .serializers import TeacherSerializer


class TeachersAPIList(generics.ListAPIView):
    """
    Показывает весь список учителей
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]


class TeachersAPIDetails(generics.RetrieveAPIView):
    """
    Выводит одного учителя по индексу
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]
