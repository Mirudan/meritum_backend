from django.urls import path
from .views import TeachersAPIList, TeachersAPIDetails

urlpatterns = [
    # отображение всего списка учителей
    path('', TeachersAPIList.as_view()),
    # отображение конкретного учителя по индексу
    path('<int:pk>/', TeachersAPIDetails.as_view()),
]