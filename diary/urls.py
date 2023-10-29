from django.urls import path

from .views import ScheduleAPIListCreate, ScheduleAPIRUDV, ScheduleAPIList

urlpatterns = [
    # отображение данных для расписания
    path('', ScheduleAPIList.as_view()),
    # возможность внесения данных
    path('create/', ScheduleAPIListCreate.as_view()),
    # отображение конкретных данных с возможностью внесения и изменения
    path('<int:pk>/', ScheduleAPIRUDV.as_view()),
]
