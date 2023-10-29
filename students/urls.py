from django.urls import path
from .views import StudentObtainTokenView

urlpatterns = [
    path('login/', StudentObtainTokenView.as_view(), name='student-obtain-token'),
]