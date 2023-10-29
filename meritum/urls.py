from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


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
    # получение списка API адресов
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # пути к новостям и курсам
    path('api/v1/', include('announcements.urls')),
    # отображение данных для управления расписанием
    path('api/v1/schedule/', include('diary.urls')),
    path('api/v1/admins/', include('admins.urls')),
    path('api/v1/students/', include('students.urls'))
]
