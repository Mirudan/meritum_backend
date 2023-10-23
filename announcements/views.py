from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from announcements.models import News
from announcements.serializers import NewsSerializer


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
