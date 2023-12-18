from django.urls import path
from .views import StudentsAPIList, StudentAPIList

urlpatterns = [
    # path('login/', StudentObtainTokenView.as_view(), name='student-obtain-token'),
    # отображение всего списка студентов
    path('', StudentsAPIList.as_view()),
    # отображение конкретного студента
    path('<int:pk>/', StudentAPIList.as_view()),
]
