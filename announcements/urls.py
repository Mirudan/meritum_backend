from django.urls import path

from .views import NewsAPIList, NewsAPIDetails, CourseAPIList, CourseAPIDetails

urlpatterns = [
    # отображение всего списка новостей
    path('newslist/', NewsAPIList.as_view()),
    # отображение конкретной новости по индексу
    path('newslist/<int:pk>/', NewsAPIDetails.as_view()),
    # отображение списка объявлений о доп курсах
    path('courses/', CourseAPIList.as_view()),
    # отображение новости доп курса по индексу
    path('courses/<int:pk>/', CourseAPIDetails.as_view()),
]