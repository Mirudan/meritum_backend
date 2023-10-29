from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from announcements.models import News, Course
from announcements.serializers import NewsSerializer, CourseSerializer


class NewsAPIList(generics.ListAPIView):
    """
    Показывает весь список новостей
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsAPIDetails(generics.RetrieveAPIView):
    """
    Выводит одну новость по индексу
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CourseAPIList(generics.ListAPIView):
    """
    Показывает весь список объявлений о доп курсах
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAPIDetails(generics.RetrieveAPIView):
    """
    Выводит одно сообщение о доп курсах по индексу
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
