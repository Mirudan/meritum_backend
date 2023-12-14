from django.urls import path

from .views import ScheduleAPIListCreate, ScheduleAPIRUDV, ScheduleAPIList, MarkAPIList, MarkAPIListCreate

urlpatterns = [
    # отображение данных для расписания
    path('schedule/', ScheduleAPIList.as_view()),
    # возможность внесения данных
    path('schedule/create/', ScheduleAPIListCreate.as_view()),
    # отображение конкретных данных с возможностью внесения и изменения
    path('schedule/create/<int:pk>/', ScheduleAPIRUDV.as_view()),
    # отображение всех оценок
    path('mark/', MarkAPIList.as_view()),
    # отображение всех оценок c возможностью внесения данных
    path('mark/create/', MarkAPIListCreate.as_view()),
]
