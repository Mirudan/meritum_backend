from django.urls import path
from .views import TeachersAPIList, TeachersAPIDetails

urlpatterns = [
    # отображение всего списка учителей
    path('teacherslist/', TeachersAPIList.as_view()),
    # отображение конкретного учителя по индексу
    path('teacherslist/<int:pk>/', TeachersAPIDetails.as_view()),
]