from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import views, permissions, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


class StudentsAPIList(generics.ListAPIView):
    """
    Отображение всех студентов
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentAPIList(generics.RetrieveAPIView):
    """
    отображение конкретного студента
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
