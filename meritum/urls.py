from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from announcements.views import NewsAPIList, NewsAPIDetails, CourseAPIList, CourseAPIDetails
from diary.views import ScheduleAPIList, ScheduleAPIRUDV, ScheduleAPIListCreate

schema_view = get_schema_view(
    openapi.Info(
        title="Meritum API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # отображение всего списка новостей
    path('api/v1/newslist/', NewsAPIList.as_view()),
    # отображение конкретной новости по индексу
    path('api/v1/newslist/<int:pk>/', NewsAPIDetails.as_view({'get': 'retrieve'})),
    # отображение списка объявлений о доп курсах
    path('api/v1/courses/', CourseAPIList.as_view()),
    # отображение новости доп курса по индексу
    path('api/v1/courses/<int:pk>/', CourseAPIDetails.as_view({'get': 'retrieve'})),
    # отображение данных для расписания
    path('api/v1/schedule/', ScheduleAPIList.as_view()),
    # возможность внесения данных
    path('api/v1/schedule/create/', ScheduleAPIListCreate.as_view()),
    # отображение конкретных данных с возможностью внесения и изменения
    path('api/v1/schedule/<int:pk>/', ScheduleAPIRUDV.as_view()),
]
