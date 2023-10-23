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


class NewsAPIDetails(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        """
        Выводит одну новость по индексу
        """
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response(status=404)

        serializer_class = NewsSerializer(news)
        return Response(serializer_class.data)


class CourseAPIList(generics.ListAPIView):
    """
    Показывает весь список объявлений о доп курсах
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAPIDetails(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        """
        Выводит одно сообщение о доп курсах по индексу
        """
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=404)

        serializer_class = CourseSerializer(course)
        return Response(serializer_class.data)
